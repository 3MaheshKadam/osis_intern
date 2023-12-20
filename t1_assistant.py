#  pip install SpeechRecognition pyttsx3 pyowm requests 
# pip install pipwin
# pipwin install pyaudio
# "paste at the terminal "
import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import pyowm

# Setting up text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Speech recognition function
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Do not understand!! Try again")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return ""

# # Email sending function
# def send_email(receiver_email, subject, body):
#     # Replace these with your own email credentials
#     sender_email = "abc@gmail.com"
#     sender_password = "123456"

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         message = f"Subject: {subject}\n\n{body}"
#         server.sendmail(sender_email, receiver_email, message)
#         server.quit()
#         speak("Email sent successfully.")
#     except Exception as e:
#         speak(f"Sorry, an error occurred: {str(e)}")

# Set your OpenWeatherMap API key
owm_api_key = "501b3c4f31b2387ecf99e7aaa58136b2"

# Weather update function
def get_weather(city):
    owm = pyowm.OWM(owm_api_key)
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')["temp"]
    status = w.get_status()

    speak(f"The weather in {city} is {status} with a temperature of {temperature} degrees Celsius.")

# Main function
def main():
    speak("Hello! How can I assist you today?")

    while True:
        user_input = recognize_speech()

        if "hello" in user_input:
            speak("Hello! How can I help you?")
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        elif "date" in user_input:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today is {current_date}")
        elif "send email" in user_input:
            speak("Whom do you want to send the email to?")
            receiver_email = recognize_speech()
            speak("What is the subject of the email?")
            email_subject = recognize_speech()
            speak("What should be the content of the email?")
            email_body = recognize_speech()
            send_email(receiver_email, email_subject, email_body)
        elif "weather" in user_input:
            speak("Sure, in which city?")
            city = recognize_speech()
            get_weather(city)
        elif "exit" in user_input or "bye" in user_input:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat or ask something else?")

if __name__ == "__main__":
    main()
