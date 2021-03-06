"""
RPS ver 1.3
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
import sys

CHOICES = ("rock", "paper", "scissor")
#sets CHOICES to have values
RUNA = ("yes", "no")
#sets RUNA to have values yes and no
RUNT = 0

def print_slow(str0):
    """typing effect animation"""
    for letter in str0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)
    print ""

def print_load(str1, str2, str3):
    """Loading animation"""
    for i in range(str1):
        print str3,
        time.sleep(str2)
    print ""

print_load(10, 0.1, ".")
print_slow("Welcome to a rock, paper and scissor game, were you fight the computer.")
#welcome text
RUN = raw_input("Start game?")
#input for the user to set RUN
COMPUTERWINS = 0
PLAYERWINS = 0

while RUN != "no":
    #loops as long RUN is not no
    if RUN == "yes":
        RUNT = 1
        PLAYERNAME = raw_input("Choose a player name:")
        print ""
        print_slow("Running version: 1.3")
        print_slow("Mode: Singleplayer")
        time.sleep(0.1)
        print "Name choosen:", PLAYERNAME
        print_slow("Opponent: Computer")
        print ""
        print_slow("Game is starting")
        print_load(3, 0.5, ".")
        print ""
        time.sleep(1.5)
    while RUN == "yes":
        #loops as long RUN id is set as yes
        COMPUTER = random.choice(CHOICES)
        #make a random number between 0 and 10
        PLAYER = raw_input("Pick: rock, paper, scissor; or use quit to exit the game: ")
        #input for the user to guess a number
        while PLAYER not in CHOICES:
            if PLAYER == "hack":
                print "The computer choosed", COMPUTER
                PLAYER = raw_input("Pick: rock, paper, scissor; or use quit to exit the game: ")
            elif PLAYER == "quit":
                RUN = "no"
                break
            elif PLAYER not in CHOICES:
                print "Please use rock, paper, scissor to pick, or use quit to exit the game"
                PLAYER = raw_input("Pick: rock, paper, scissor; or use quit to exit the game: ")
        if RUN == "yes":
            print ""
            print PLAYERNAME, "vs Computer"
            time.sleep(2)
            print ""
            print PLAYERNAME, "choose", PLAYER
            time.sleep(1)
            print ""
            print "Computer choose", COMPUTER
            time.sleep(0.5)
            print ""
            if PLAYER == COMPUTER:
                print "Its a draw!"
            else:
                if PLAYER == "rock":
                    if COMPUTER == "paper":
                        print "Computer wins!"
                        COMPUTERWINS = COMPUTERWINS + 1
                    else:
                        print PLAYERNAME, "wins!"
                        PLAYERWINS = PLAYERWINS + 1
                if PLAYER == "paper":
                    if COMPUTER == "scissor":
                        print "Computer wins!"
                        COMPUTERWINS = COMPUTERWINS + 1
                    else:
                        print PLAYERNAME, "wins!"
                        PLAYERWINS = PLAYERWINS + 1
                if PLAYER == "scissor":
                    if COMPUTER == "rock":
                        print "Computer wins!"
                        COMPUTERWINS = COMPUTERWINS + 1
                    else:
                        print PLAYERNAME, "wins!"
                        PLAYERWINS = PLAYERWINS + 1
            print ""
            print "Computer have", COMPUTERWINS, "points"
            print PLAYERNAME, "have", PLAYERWINS, "points"
        print ""
    while RUN not in RUNA:
        #loops as long you dont type yes or no
        print "That is not an answer, please use yes or no to answear the question"
        RUN = raw_input("Start game?")
        print ""

if RUN == "no":
    #game stopped
    print ""
    print_slow("Game not running")
    print ""
    if RUNT == 1:
        time.sleep(2)
        print "Computer have", COMPUTERWINS, "points"
        print PLAYERNAME, "have", PLAYERWINS, "points"
        print ""
        time.sleep(1)
        if PLAYERWINS == COMPUTERWINS:
            print "The game ended in a draw!"
        elif PLAYERWINS > COMPUTERWINS:
            print PLAYERNAME, "won the game!"
        else:
            print "Computer won the game!"
    time.sleep(2)
    print ""
    print ""
    print "Made by:"
    print "Magnar Hole Polden"
    print ""
    time.sleep(10)
