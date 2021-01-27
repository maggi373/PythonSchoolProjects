# coding=UTF-8
"""
TTT ver 1.1
An Tic Tac Toe game

Made by
Magnar Hole Polden

"""

import random
import sys
import time

BOARDEX = [1, 2, 3, 4, 5, 6, 7, 8, 9]
BOARD = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
WON = ""
CC = 0
STATUS = "NOT OK"
CUCANCEL = "Good"
CUCANCEL2 = ""
CUCANCEL3 = ""
WHO = "Error"
VAL = ["X", "O"]
COMPUTERWINS = 0
PLAYER1WINS = 0
PLAYER2WINS = 0
ANS = "Good"
RUNT = 0
ALT = ""
ASP = 1
BR = 0
MODES = ["singleplayer", "multiplayer"]
MOD = 0
PLAYER2 = ""
CC2 = 0
WHOS = 0

def print_slow(str0):
    """typing effect animation"""
    for letter in str0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)
    print

def print_load(str1, str2, str3):
    """Loading animation"""
    for IFF in range(str1):
        print str3,
        time.sleep(str2)
    print

def graphicsboard(str1):
    """The graphics for the board"""
    print "     |     |"
    print " ", str1[0], " | ", str1[1], " | ", str1[2]
    print "     |     |"
    print "-----------------"
    print "     |     |"
    print " ", str1[3], " | ", str1[4], " | ", str1[5]
    print "     |     |"
    print "-----------------"
    print "     |     |"
    print " ", str1[6], " | ", str1[7], " | ", str1[8]
    print "     |     |"

def choice(str1, str2, str3, str4, str5):
    """Converts choice to board"""
    global CUCANCEL2
    global CUCANCEL3
    IFF = str1 - 1
    if str2[IFF] == " ":
        str2[IFF] = str3
        if str5 == CUCANCEL2 or str5 == CUCANCEL3:
            if str5 == CUCANCEL2:
                CUCANCEL2 = "Good"
            if str5 == CUCANCEL3:
                CUCANCEL3 = "Good"
    else:
        graphicsboard(str4)
        if str5 == CUCANCEL2 or str5 == CUCANCEL3:
            if str5 == CUCANCEL2:
                CUCANCEL2 = "STOP"
            if str5 == CUCANCEL3:
                CUCANCEL3 = "STOP"
        print "Place already taken"
        str1 = raw_input("Pos: ")

def choiceg(hur1, hur2, hur3, hur4, hur5, hur6, hur7):
    """
    hur1 = player1
    hur2 = cc
    hur3 WON
    hur4 STATUS
    hur5 cucancel
    hur6 BOARD
    hur7 type of x or o
    """
    global hur3
    global hur4
    HURA = "False"
    while HURA != "True":
        hur2 = raw_input("Pos: ")
        if hur2 == "quit":
            hur3 = "WON"
        elif hur2.isdigit() == False:
            #only use numbers code
            print "USE ONLY NUMBERS!"
        elif hur2.isdigit() == True:
            #supports negative numbers and positive numbers
            hur2 = int(hur2)
            #translates from string to a variable
            if hur2 not in range(1, 10):
                #must have
                if hur2 <= 9:
                    print "The number has a lesser value"
                if hur2 >= 1:
                    print "The number has a higher value"
                #input for the user to try again
            else:
                IFF = hur2 - 1
                if hur6[IFF] == " ":
                    hur6[IFF] = hur7
                    HURA == "True"
                else:
                    graphicsboard(hur6)
                    print "Place already taken"
                hur4 = "OK"
        HURA == "False"

def co(str1):
    """computer engine"""
    print "Computers turn"
    global STATUS2
    AFF = 0
    while AFF != 1:
        CFF = random.randint(0, 8)
        if BOARD[CFF] == " ":
            BOARD[CFF] = "O"
            graphicsboard(str1)
            AFF = 1
            CUCANCEL = "STOP"
            STATUS2 = "OK"

def wut(str1, str2, str3):
    """Checks of somone won"""
    global WON
    global WHO
    global BR
    global PLAYER1
    global PLAYER2
    global WHOS
    if str1 == "X" and str2 == "X" and str3 == "X":
        WON = "WON"
        WHO = PLAYER1
        WHOS = 1
        BR = 1
    elif str1 == "O" and str2 == "O" and str3 == "O":
        WON = "WON"
        WHO = PLAYER2
        WHOS = 2
        BR = 1
    else:
        WHOS = 0

print "--- TicTacToe ---"
print
print "This program is in alpha, there are many bugs"
print_load(10, 0.1, ".")
print_slow("Tcalc VER: 1.1")

print "The layout as follows"
graphicsboard(BOARDEX)
print

MODE = raw_input("What mode shall be used: ").strip().lower()
while MODE not in MODES:
    print "You can only select", MODES
    MODE = raw_input("What mode shall be used: ").strip().lower()
if MODE == "singleplayer":
    MOD = 1
    NAME = "Choose your name:"
    PLAYER2 = "Computer"
elif MODE == "multiplayer":
    MOD = 2
    NAME = "Player 1 name: "
PLAYER1 = raw_input(NAME)
if MOD == 2:
    PLAYER2 = raw_input("Player 2 name: ")
while ALT != "done":
    print "Mode running: ", MODE
    while WON != "WON":
        if ASP == 1:
            ASP = 0
            BOARD = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            if MOD == 1:
                co(BOARD)
            BR = 0
        print PLAYER1, "turn"
        graphicsboard(BOARD)
        choiceg(PLAYER1, CC, WON, STATUS, CUCANCEL2, BOARD, "X")
        if STATUS == "OK":
            graphicsboard(BOARD)
            wut(BOARD[0], BOARD[1], BOARD[2])
            wut(BOARD[3], BOARD[4], BOARD[5])
            wut(BOARD[6], BOARD[7], BOARD[8])
            wut(BOARD[0], BOARD[3], BOARD[6])
            wut(BOARD[1], BOARD[4], BOARD[7])
            wut(BOARD[2], BOARD[5], BOARD[8])
            wut(BOARD[0], BOARD[4], BOARD[8])
            wut(BOARD[2], BOARD[4], BOARD[6])
            if BOARD[0] in VAL and BOARD[1] in VAL and BOARD[2] in VAL and BOARD[3] in VAL and BOARD[4] in VAL and BOARD[5] in VAL and BOARD[6] in VAL and BOARD[7] in VAL and BOARD[8] in VAL:
                WON = "WON"
                WHO = "TIE"
                CUCANCEL = "STOP"
                break
            if BR == 1:
                break
            if CUCANCEL != "STOP" and MOD == 1:
                co(BOARD)
            if CUCANCEL != "STOP" and MOD == 2:
                while CC2 not in range(1, 10):
                    #loops as long the number is wrong
                    print PLAYER2, "turn"
                    CC2 = raw_input("Pos: ")
                    if CC2 == "quit":
                        WON = "WON"
                        break
                    elif CC2.isdigit() == False:
                        #only use numbers code
                        print "USE ONLY NUMBERS!"
                        CC2 = raw_input("Try again:")
                    elif CC2.isdigit() == True:
                        #supports negative numbers and positive numbers
                        CC2 = int(CC2)
                        #translates from string to a variable
                        if CC2 not in range(1, 10):
                            #must have
                            if CC2 <= 9:
                                print "The number has a lesser value"
                            if CC2 >= 1:
                                print "The number has a higher value"
                            #input for the user to try again
                        else:
                            while CUCANCEL3 != "Good":
                                choice(CC2, BOARD, "O", BOARD, CUCANCEL3)
                            STATUS = "OK"
                            break
            CC2 = 0
            CC = 0
            STATUS = "NOT OK"
            graphicsboard(BOARD)
            wut(BOARD[0], BOARD[1], BOARD[2])
            wut(BOARD[3], BOARD[4], BOARD[5])
            wut(BOARD[6], BOARD[7], BOARD[8])
            wut(BOARD[0], BOARD[3], BOARD[6])
            wut(BOARD[1], BOARD[4], BOARD[7])
            wut(BOARD[2], BOARD[5], BOARD[8])
            wut(BOARD[0], BOARD[4], BOARD[8])
            wut(BOARD[2], BOARD[4], BOARD[6])
            if BOARD[0] in VAL and BOARD[1] in VAL and BOARD[2] in VAL and BOARD[3] in VAL and BOARD[4] in VAL and BOARD[5] in VAL and BOARD[6] in VAL and BOARD[7] in VAL and BOARD[8] in VAL:
                WON = "WON"
                WHO = "TIE"
                break
            STATUS2 = "NOT OK"
            CUCANCEL2 = ""
            CUCANCEL3 = ""
    if WON == "WON":
        #game stopped
        print
        graphicsboard(BOARD)
        print
        time.sleep(2)
        print
        if WHOS == 2:
            COMPUTERWINS = COMPUTERWINS + 1
            print PLAYER2, "won the game!"
        elif WHOS == 1:
            PLAYER1WINS = PLAYER1WINS + 1
            print PLAYER2, "won the game!"
        if WHOS == 0:
                print "Its a tie"
        print
        RUNT = 1
        while ANS == "Good":
            MORE = raw_input("Do you want to contiue?: ").strip().lower()
            if MORE == "yes":
                WON = ""
                ANS = "df"
                ASP = 1
            if MORE == "no":
                ALT = "done"
                ANS = "df"
            else:
                print "You can only use yes or no to answer"
print
print_slow("TicTacToe not running")
if RUNT == 1:
    time.sleep(2)
    print PLAYER2, "have", COMPUTERWINS, "points"
    print PLAYER1, "have", PLAYER1WINS, "points"
    print ""
    time.sleep(1)
    if PLAYER1WINS == COMPUTERWINS:
        print "The game ended in a draw!"
    elif PLAYER1WINS > COMPUTERWINS:
        print PLAYER1, "won the game!"
    else:
        print PLAYER2, "won the game!"
time.sleep(2)
print
print "Made by:"
print "Magnar Hole Polden"
print
time.sleep(5)
