import re
import os


def check(password):
    # returns true if all conditions are met, otherwise returns reason(s)
    # check if password is at least 8 chars long
    reasons = []
    if len(password) < 8:
            reasons.append("be longer than 8 characters long")
    # check if password has an uppercase char
    if not re.search(r'[A-Z]', password):
         reasons.append("contain an uppercase character")
    # check if password has a lowercase char
    if not re.search(r'[a-z]', password):
         reasons.append("contain a lowercase character")
    # check if password has a number
    if not re.search(r'[0-9]', password):
         reasons.append("contain a number")
    # check if password has a special char
    if not re.search(r'[^A-Za-z0-9\s]', password):
         reasons.append("contain a special character")
    return reasons
    

def score(password):
     # this function will score the password out of 
     # 100 based on some arbitrary numbers I decide
     # first lets find out how many of each
     uppers = len(re.findall(r'[A-Z]', password))
     lowers = len(re.findall(r'[a-z]', password))
     numbers = len(re.findall(r'[0-9]', password))
     specials = len(re.findall(r'[^A-Za-z0-9\s]', password))
     # for now lets just print it.
     print(f'Uppers: {uppers}')
     print(f'Lowers: {lowers}')
     print(f'Numbers: {numbers}')
     print(f'Specials: {specials}')


def clear():
     if os.name == 'nt':
         os.system('cls')
     else:
         os.system('clear')

if __name__ == '__main__':
    # main
    clear()
    while True:
        # get user input
        user_input = input('Please input your password: \n')
        checked = check(user_input)
        

        if len(checked) > 0:
             #password failed, list reasons
             s = "There are some things you could improve: \n"
             for i, reason in enumerate(checked):
                  s += f'{i+1}. Your password must {reason}\n'
             print(s)
        else:
             print('congrats on your good(enough) password')
        score(user_input)
        



        