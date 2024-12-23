import re
import time
import os
import math
from collections import Counter
import requests


def check(password):
    # returns true if all conditions are met, otherwise returns reason(s)
    # check if password is at least 8 chars long
    reasons = []

    if len(password) < 8:
        reasons.append("be longer than 8 characters long")

    # check if password has an uppercase char
    if not re.search(r"[A-Z]", password):
        reasons.append("contain an uppercase character")

    # check if password has a lowercase char
    if not re.search(r"[a-z]", password):
        reasons.append("contain a lowercase character")

    # check if password has a number
    if not re.search(r"[0-9]", password):
        reasons.append("contain a number")

    # check if password has a special char
    if not re.search(r"[^A-Za-z0-9\s]", password):
        reasons.append("contain a special character")


    return reasons


def score(password):
    # this function will score the password base on the amount of entropy, or randomness it has

    #count the occurances of each character
    char_count = Counter(password)
    probabilities = [counts/len(password) for counts in char_count.values()]
    # count the entropy of each character, then multiply by the number of characters
    entropy = -sum(p * math.log2(p) for p in probabilities) * len(password)

    # so the magic numbers here are 10 digits(0-9)
    # 26 lower case characters(a-z)
    # 26 uppercase characters(A-Z)
    # around 32 special chars ( ! @ # $ % ^ & * etc )

    # so the whole formula is (length of data * log2(# of possibilities))
    max_entropy = (len(password) * math.log2(10+26+26+32))

    print(f"Entropy: {entropy}\nMax Entropy for len({len(password)}): {max_entropy}")

    # normalize
    n_entropy = entropy / max_entropy

    print(f"Normalized Entropy: {n_entropy}")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_list(file_path="commons_passwords.txt"):
    p_list = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            p_list = [line.strip() for line in file]
    else:
        try:
            r = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")
            with open(file_path, 'w+') as file:
                file.writelines(r.text)
        except Exception as e:
            print(f'something went wrong, lazy exception catch. this is at the get list function\n{e}')
            return False
    return p_list
        


def test_dictionary(password):
    # this function will test the password against a list of common passwords
    commons = get_list()
    if password in commons:
        print(f'\n\n\n\n\nyou LOSE\n\n\n\n\n')


if __name__ == "__main__":
    # main
    clear()
    print(
        f"NEVER EVER under ANY circumstances enter your password ANYWHERE!!\nUnless you FULLY TRUST the page or application"
    )
    print(f"The source code for this project is fully available")
    print(
        f"It will NOT steal your password, but that does not mean you should trust it!"
    )
    time.sleep(5)
    while True:
        # get user input
        user_input = input("Please input your password: \n")
        if len(user_input) <= 0:
            print("\nYou actually have to enter a password.\n")
            continue
        checked = check(user_input)
        clear()
        print(f"Your password: {user_input}\n\n")
        if len(checked) > 0:
            # password failed, list reasons
            s = "There are some things you could improve: \n"
            for i, reason in enumerate(checked):
                s += f"{i+1}. Your password must {reason}\n"
            print(f"\n{s}\n")
        else:
            print("\ncongrats on your good(enough) password\n")
        score(user_input)
        i = input("\nWould you like to check password against list of common passwords? [(Y)/n]\nMake your selection then press enter. ")
        if len(i) <= 1 and 'n' in i:
            continue
        else:
            test_dictionary(user_input)
        
