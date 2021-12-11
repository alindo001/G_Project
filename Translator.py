from greaterthan20 import *



user_input = input("Enter a number 1 through 59 to output the Spanish translation or type exit to end the program >>>")

while user_input != "exit":

    if user_input in numbersdict:
        print(numbersdict[user_input])
    elif "twenty" in user_input:
        twenty(user_input)
    elif "thirty" in user_input:
        thirty(user_input)
    elif "forty" in user_input:
        forty(user_input)
    elif "fifty" in user_input:
        fifty(user_input)




    user_input = (input("Enter a number 1 through 59 to output the Spanish translation or type exit to end program >>> "))