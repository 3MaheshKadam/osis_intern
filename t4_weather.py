import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.RequestException as e:
        print(f"Error connecting to the weather API: {e}")
        return None

def display_weather(data):
    if data:
        print("\nCurrent Weather:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Conditions: {data['weather'][0]['description']}")
    else:
        print("Failed to retrieve weather data.")

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your actual OpenWeatherMap API key
    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
