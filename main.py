# _/\/\/\/\/\_
# | -      - |
# \___-___-__/
# 100% man made code!
# 0% AI slop!

import secrets
import random
import pyperclip
import threading

# intentionally dramatic sentences giving security advice/telling jokes.
random_sentences = [
    "Don't share it!",
    ". . .it's a secret!",
    "A shiny new password!",
    "I bet you can't crack it!",
    "Save it to a password manager!",
    "Use 2FA!",
    "John rips through these!",
    "Be careful!",
    "Perfect for encrypted files!",
    "Don't trust anyone with it!",
    "Write it down!",
    "This is as strong as a brick wall!",
    "Try to guess this!",
    "Never give it to anyone, even if they say they're from a service you use.",
    "You should be the only one with it!",
    "This should definitely stay private!",
    "Don't get phished!",
    "This is uncrackable! At least for now. *cough* Quantum computing."
]

def generate_password(char_count):
    char_string = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        r"""!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    )
    return ''.join(
        secrets.choice(char_string)
        for _ in range(char_count)
    )

def print_intro():
    print("\033[0;92m-__________________________________________________-")
    print("|  brought to you by: zero____                     |")
    print("|    Password generator (\033[31mcryptographically secure\033[0;92m) |")
    print("-__________________________________________________-\033[0m")

def copy_password(password):
    pyperclip.copy(password)
    timer = threading.Timer(120, pyperclip.copy, args=("",))

    timer.start()

def password_msg(password):
    print("[XuX] Here's your password!")
    copy_password(password)
    print("Password copied to clipboard, deleting in 2 minutes, make it quick!")
    print(random.choice(random_sentences))

def get_password_length():
    while True:
        try:
            char_count = int(input("Enter the length of the password: "))

            if char_count < 1:
                print("Positive number required!")
                continue

            if char_count > 1000:
                print("Password length input can't exceed more than 1000 characters!")
                continue

            return char_count

        except ValueError:
            print("Excuse me? Is that a joke? Please enter a whole number.")

def start():
    print_intro()
    char_count = get_password_length()
    password = generate_password(char_count)
    password_msg(password)

if __name__ == "__main__":
    start()