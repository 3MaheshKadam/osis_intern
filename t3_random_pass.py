import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character set.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters (y/n)? ").lower() == 'y'
        use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
        use_symbols = input("Include symbols (y/n)? ").lower() == 'y'
    except ValueError:
        print("Error: Please enter a valid number for the password length.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
