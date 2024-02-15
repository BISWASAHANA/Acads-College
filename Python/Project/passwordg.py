#Write a Python program to build a secure password generator.

import string
import secrets

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
            and any(c in string.punctuation for c in password)
            and not any(c in "Il1O0" for c in password)):
            return password

def main():
    password_length = int(input("Enter the desired password length (default is 8): "))
    if password_length <= 0:
        print("Password length should be a positive integer. Using the default length of 8.")
        password_length = 8

    password = generate_password(password_length)
    print("Generated password: ", password)

if __name__ == "__main__":
    main()
