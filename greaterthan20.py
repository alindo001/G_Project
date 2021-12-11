from numbersdict import *


def print(param):
    pass


def twenty(user_input):
    if "twenty" in user_input:
        twenty_string = user_input.replace("twenty", "")
        if twenty_string.strip() in numbersdict:
            print("venti" + numbersdict[twenty_string.strip()])
    return

