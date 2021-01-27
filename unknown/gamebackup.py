"""
RPS ver 1.1
A simple rock, paper, scissor game

Made by
Magnar Hole Polden

"""

# -*- coding: cp1252 -*-

#A simple rock, paper, scissor game
#Made by:
#Magnar Hole Polden

import random
#import random reg
import time
#imports time

CHOICES = ("rock", "paper", "scissor")
#sets CHOICES to have values
RUNA = ("yes", "no")
#sets RUNA to have values yes and no

print "Welcome to a rock, paper and scissor game, were you fight the computer."
#welcome text
RUN = raw_input("Start game?")
#input for the user to set RUN

def engine(X, A):
    if X == A:
        print "It's a tie!"
    if A == "rock":
        if X == "scissor":
            print "You won! The computer choosed", X
        else:
            print "You lost, the computer choosed", X
    if A == "paper":
        if X == "rock":
            print "You won! The computer choosed", X
        else:
            print "You lost, the computer choosed", X
    if A == "scissor":
        if X == "paper":
            print "You won! The computer choosed", X
        else:
            print "You lost, the computer choosed", X

while RUN != "no":
    #loops as long RUN is not no
    while RUN == "yes":
        #loops as long RUN id is set as yes
        X = random.choice(CHOICES)
        #make a random number between 0 and 10
        A = raw_input("Pick: rock, paper or scissor:")
        #input for the user to guess a number
        while A not in CHOICES:
            if A == "hack":
                print "The computer choosed", X
                A = raw_input("Pick: rock, paper or scissor:")
            if A not in CHOICES:
                print "Please use rock, paper or scissor to pick"
                A = raw_input("Pick: rock, paper or scissor:")
        if A in CHOICES:
            engine(X, A)
        RUN = raw_input("Restart game?")
        #user can choose to restart game
    while RUN not in RUNA:
        #loops as long you dont type yes or no
        print "That is not an answear, please use yes or no to answear the question"
        RUN = raw_input("Start game?")

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
