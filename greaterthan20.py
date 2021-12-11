from numbersdict import *




def twenty(user_input):
    if "twenty" in user_input:
        twenty_string = user_input.replace("twenty", "")
        if twenty_string.strip() in numbersdict:
            print("veinti" + numbersdict[twenty_string.strip()])
    return


def thirty(user_input):
    if "thirty" in user_input:
        thirty_string = user_input.replace("thirty", "")
        if thirty_string.strip() in numbersdict:
            print("treinta y " + numbersdict[thirty_string.strip()])
    return


def forty(user_input):
    if "forty" in user_input:
        forty_string = user_input.replace("forty", "")
        if forty_string.strip() in numbersdict:
            print("cuarenta y " + numbersdict[forty_string.strip()])
    return


def fifty(user_input):
    if "fifty" in user_input:
        fifty_string = user_input.replace("fifty", "")
        if fifty_string.strip() in numbersdict:
            print("cincuenta y " + numbersdict[fifty_string.strip()])
    return