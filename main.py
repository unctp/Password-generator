# _/\/\/\/\/\_
# | -      - |
# \___-___-__/
#
# author: zero___/pira8
# my site: https://noname.pira8.workers.dev/
# license: MIT
# 
# Dear future me, never forget the day you wrote this script. 8/2/26 
#
# "Yes, I KNOW I used too many comments. The source code is part of the experience."
# "I could've done it the boring way, but where's the fun in that?"
# "Yes, I know I could've make this three lines."
# context for people who aren't interested in cybersecurity, "John rips through these!", john was referring to John The Ripper, a password cracking utility, "these" was referring to passwords themselves.
# I enjoyed this project.
# feature list:
# animated text
# ansi codes
# password generation
# automatic copying to clipboard and automatic deletion after 2 minutes
# random messages on generation
# multi-platform support
#
# requirements:
# pyperclip - clipboard handling
# threading - timers
# and eventually: flask - web UI
#
# Minimal exposure model, password is copied to clipboard directly and never printed to the screen.
#
# I'll probably make a web UI using flask for this later
# enjoy!
# 

import secrets
import random # for "non critical" randomization
import threading
import sys
import time

if sys.platform in ("win32", "linux", "darwin"):
    import pyperclip
else:
    pyperclip = None
    print_password = True

# "I know the serious security advice, but I'm going to make it entertaining."
# intentionally dramatic sentences giving security advice/telling jokes.
random_sentences = [
    "\nDon't share it!\n",
    "\n. . .it's a secret!\n",
    "\nA shiny new password!\n",
    "\nI bet you can't crack it!\n",
    "\nSave it to a password manager!\n",
    "\nUse 2FA!\n",
    "\nJohn rips through these!\n",
    "\nBe careful!\n",
    "\nPerfect for encrypted files!\n",
    "\nDon't trust anyone with it!\n",
    "\nWrite it down!\n",
    "\nThis is as strong as a brick wall!\n",
    "\nTry to guess this!\n",
    "\nNever give it to anyone, even if they say they're from a service you use.\n",
    "\nYou should be the only one with it!\n",
    "\nThis should definitely stay private!\n",
    "\nDon't get phished!\n",
    "\nThis is uncrackable! At least for now. *cough* Quantum computing.\n",
    "\nDon't let Big Brother see it!\n",
    "\nHopefully this isn't generated for a platform that gives your data to data brokers...\n",
    "\nDon't fall for a hacker's favorite sport.\n",
    "\nI haven't been here the whole time. I ran-some-ware!\n"
    "\nOh boy, it would definitely suck if it was cracked by a hydra.\n"
]

# "Why did the password lack confidence? It was insecure."
def generate_password(char_count):
    # the characters being used for password generation that secrets.choice picks securely
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

# a simple typing animation
def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def print_intro():
    typing("\033[0;92m-__________________________________________________-\n")
    typing("|  brought to you by: zero____                     |\n")
    typing("|  Password generator (\033[31mUses a CSPRNG\033[0;92m)              |\n")
    print("-__________________________________________________-\033[0m\n")

# clipboard handling
def copy_password(password):
    pyperclip.copy(password)

    def clear_clipboard():
        try:
            if pyperclip.paste() == password:
                pyperclip.copy("")
        except Exception:
            pass

    timer = threading.Timer(120, clear_clipboard)
    timer.daemon = True
    timer.start()

# message that displays after successful password generation
def password_msg(password):
    typing("[XuX] Here's your password!\n")
    if not print_password:
        print_option = input("would you like to print the password to the screen? (y/n): ")

        if print_option == "y":
            print(f"{password}")
        elif print_option == "n":
            copy_password(password)
            typing("\033[0;92mPassword copied to clipboard, deleting in 2 minutes, make it quick!\033[0m")
        else:
            print("Invalid input.")
    else:
        print(f"{password}")
    typing(random.choice(random_sentences),) # proper usage of random.choice() use secrets.choice for anything sensitive! its always important to use the right library for the right job.

# take and validate password length input
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
        except KeyboardInterrupt:
            print("\nWow, why'd you run it?")
            exit()

def exit_message():
    print("Goodbye.")
    exit()

def again():
    answer = input("Do you want to generate another password? (y/n): ")
    return answer == "y"

# beginning of program
def start():
    # execute functions in order of print_intro() > get_password_length() > generate_password() > password_msg() > again()
    print_intro()
    while True:
        char_count = get_password_length()
        password = generate_password(char_count)
        password_msg(password)
        if not again():
            exit_message()

if __name__ == "__main__":
    start()
