from numbersdict import *



user_input = (input("Enter a number 1 through 20 to output the Spanish translation or type exit to end the program >>>"))

while user_input != "exit":

    if user_input in numbersdict:
        print(numbersdict[user_input])

    user_input = (input("Enter a number 1 through 20 to output the Spanish translation "))