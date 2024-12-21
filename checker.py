import re
import time
import os
import math


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


# count the number of times each character appears in the password
def count(password):
    # iterate thru the string
    counts = {}
    for char in password:
        if char in counts.keys():
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def score(password):
    # this function will score the password base on the amount of entropy, or randomness it has
    #count the occurances of each character
    char_count = count(password)
    probabilities = [counts/len(password) for counts in char_count.values()]
    entropy = 0
    for p in probabilities:
        entropy -= -p * math.log2(p)
    print(f"Entropy: {entropy}")

    # so the magic numbers here are 10 digits(0-9)
    # 26 lower case characters(a-z)
    # 26 uppercase characters(A-Z)
    # around 32 special chars ( ! @ # $ % ^ & * etc )

    # so the whole formula is (length of data * log2(# of possibilities))
    max_entropy = len(password) * math.log2(10 + 26 + 26 + 32)

    print(f"Entropy: {entropy}")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


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
        input("\n\nPress [ENTER] to try another password...")
