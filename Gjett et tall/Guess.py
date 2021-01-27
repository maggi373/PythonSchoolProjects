"""
GUESS ver 1.3
A simple guess me game

Made by
Magnar Hole Polden

"""

# -*- coding: cp1252 -*-


import random
#import random reg
import time
#imports time

RUNA = ("yes", "no")
#sets RUNA to have values yes and no
print "Welcome to a guess game, were you guess the number that the computer has."
#welcome text
RUN = raw_input("Start game?").strip().lower()
#input for the user to set RUN

while RUN != "no":
    #loops as long RUN is not no
    while RUN == "yes":
        #loops as long RUN id is set as yes
        X = random.randint(0, 10)
        #make a random number between 0 and 10
        A = raw_input("I have a number between 0 and 10, guess:")
        #input for the user to guess a number
        while A != X:
            #loops as long the number is wrong
            if A == "hack":
                #cheat code
                print "The number is", X
                A = raw_input("Type in number:")
            if A.lstrip("-").isdigit() == False:
                #only use numbers code
                print "USE ONLY NUMBERS!"
                A = raw_input("Try again:")
            if A.lstrip("-").isdigit() == True:
                #supports negative numbers and positive numbers
                A = int(A)
                #translates from string to a variable
                if A != X:
                    #must have
                    if A > X:
                        #if a is bigger than x it does
                        if A <= 10:
                            print "The number has a lesser value"
                        else:
                            print "Too high number!"
                    if A < X:
                        #if a is smaller than x it does
                        if A >= 0:
                            print "The number has a higher value"
                        else:
                            print "Too low number!"
                    A = raw_input("Try again:")
                    #input for the user to try again
        print "CORRECT!"
        #if a is x then it prints correct!
        RUN = raw_input("Restart game?").strip().lower()
        #user can choose to restart game
    while RUN not in RUNA:
        #loops as long you dont type yes or no
        print "That is not an answear, please use yes or no to answear the question"
        RUN = raw_input("Start game?").strip().lower()

if RUN == "no":
    #game stopped
    print "game not running"
    time.sleep(2)
    print ""
    print ""
    print "Made by:"
    print "Magnar Hole Polden"
    print ""
    time.sleep(10)
