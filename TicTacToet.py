# coding=UTF-8
"""
TTT ver 1.3
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
CR = "0"
STATUS = "NOT OK"
CUCANCEL = 0
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
PLAYERSYMBOL = "EP"
COMPUTERSYMBOL = "EC"
STARTCHOICE = "o"
PLAYERNAME2 = "Computer"
GAMEMODE = "E"

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

def choice(str1, str2, str3, str4):
    """Converts choice to board"""
    global CUCANCEL
    IFF = str1 - 1
    if str2[IFF] == " ":
        str2[IFF] = str3
        CUCANCEL = "Good"
    else:
        graphicsboard(str4)
        CUCANCEL = "STOP"
        print "Place already taken"

def co(saur1):
    """computer engine"""
    print "Computers turn"
    AFF = 0
    global COMPUTERSYMBOL
    while AFF != 1:
        CFF = random.randint(0, 8)
        if BOARD[CFF] == " ":
            BOARD[CFF] = COMPUTERSYMBOL
            graphicsboard(saur1)
            AFF = 1

def wut(str1, str2, str3):
    """Checks of somone won"""
    global WON
    global WHO
    global BR
    global PLAYERSYMBOL
    global PLAYERNAME
    global PLAYERNAME2
    if str1 == PLAYERSYMBOL and str2 == PLAYERSYMBOL and str3 == PLAYERSYMBOL:
        WON = "WON"
        WHO = PLAYERNAME
        BR = 1
    if str1 == COMPUTERSYMBOL and str2 == COMPUTERSYMBOL and str3 == COMPUTERSYMBOL:
        WON = "WON"
        WHO = PLAYERNAME2
        BR = 1
    else:
        pass

def good_input(str1, str2, str3, str4, str5):
    """Sheep"""
    global CR
    global CUCANCEL
    global WON
    global WHO
    global ALT
    global STATUS
    CC = "11"
    while CC not in range(1, 10):
        #loops as long the number is wrong
        print str5, "turn"
        CC = raw_input("Pos: ")
        if CC == "quit":
            WON = "WON"
            WHO = "TIE"
            ALT = "done"
            CR = "quit"
            break
        elif CC.isdigit() is False:
            #only use numbers code
            print "USE ONLY NUMBERS!"
            CC = raw_input("Try again:")
        elif CC.isdigit() is True:
            #supports negative numbers and positive numbers
            CC = int(CC)
            #translates from string to a variable
            if CC not in range(1, 10):
                #must have
                if CC <= 9:
                    print "The number has a lesser value"
                if CC >= 1:
                    print "The number has a higher value"
                #input for the user to try again
            else:
                STATUS = "OK"
                IFF = CC - 1
                if str2[IFF] == " ":
                    str2[IFF] = str3
                    CUCANCEL = 0
                    break
                else:
                    graphicsboard(str4)
                    CUCANCEL = str1
                    print "Place already taken"
                    CC = "11"

print "--- TicTacToe ---"
print
print "This program is in alpha, there are many bugs"
print_load(10, 0.1, ".")
print_slow("Tcalc VER: 1.3")

print "The layout as follows"
graphicsboard(BOARDEX)
print

while GAMEMODE != "singleplayer" and GAMEMODE != "multiplayer":
    print "what mode shall be used, singleplayer (against a computer) or multiplayer (two players)?"
    GAMEMODE = raw_input(": ").strip().lower()
if GAMEMODE == "singleplayer":
    GAMEMODE = 0
    print "Please choose a player name"
    PLAYERNAME = raw_input(": ")
if GAMEMODE == "multiplayer":
    GAMEMODE = 1
    print "Player 1, please choose a player name"
    PLAYERNAME = raw_input("Player 1: ")
    print "Player 2, please choose a player name"
    PLAYERNAME2 = raw_input("Player 2: ")
    while PLAYERNAME == PLAYERNAME2:
        print "You cant have the same name as", PLAYERNAME
        PLAYERNAME2 = raw_input("Player 2: ")
while PLAYERSYMBOL != "X" and PLAYERSYMBOL != "O":
    print PLAYERNAME, "please select the following symbols to show your choice; X or O"
    PLAYERSYMBOL = raw_input(": ").strip().upper()
if PLAYERSYMBOL != "EP":
    if PLAYERSYMBOL == "X":
        COMPUTERSYMBOL = "O"
    if PLAYERSYMBOL == "O":
        COMPUTERSYMBOL = "X"
while ALT != "done":
    while WON != "WON":
        while STARTCHOICE != PLAYERNAME and STARTCHOICE != PLAYERNAME2:
            print "who shall begin the game?", PLAYERNAME, "or", PLAYERNAME2, "?: "
            STARTCHOICE = raw_input(": ")
        CC = 0
        STATUS = "NOT OK"
        if ASP == 1:
            ASP = 0
            BOARD = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            BR = 0
            if STARTCHOICE == PLAYERNAME2:
                if STARTCHOICE == "Computer":
                    co(BOARD)
                else:
                    good_input(2, BOARD, COMPUTERSYMBOL, BOARD, PLAYERNAME2)
                    graphicsboard(BOARD)
        if CUCANCEL != 2:
            good_input(1, BOARD, PLAYERSYMBOL, BOARD, PLAYERNAME)
            if GAMEMODE == 1:
                graphicsboard(BOARD)
        if STATUS == "OK":
            wut(BOARD[0], BOARD[1], BOARD[2])
            wut(BOARD[3], BOARD[4], BOARD[5])
            wut(BOARD[6], BOARD[7], BOARD[8])
            wut(BOARD[0], BOARD[3], BOARD[6])
            wut(BOARD[1], BOARD[4], BOARD[7])
            wut(BOARD[2], BOARD[5], BOARD[8])
            wut(BOARD[0], BOARD[4], BOARD[8])
            wut(BOARD[2], BOARD[4], BOARD[6])
            if BR == 1:
                WON = "WON"
                ASP = 1
                STARTCHOICE = ""
                break
            if BOARD[0] in VAL and BOARD[1] in VAL and BOARD[2] in VAL and BOARD[3] in VAL and BOARD[4] in VAL and BOARD[5] in VAL and BOARD[6] in VAL and BOARD[7] in VAL and BOARD[8] in VAL:
                WON = "WON"
                WHO = "TIE"
                ASP = 1
                STARTCHOICE = ""
                break
            if CUCANCEL != 1:
                if GAMEMODE == 0:
                    co(BOARD)
                if GAMEMODE == 1:
                    good_input(2, BOARD, COMPUTERSYMBOL, BOARD, PLAYERNAME2)
                    graphicsboard(BOARD)
                wut(BOARD[0], BOARD[1], BOARD[2])
                wut(BOARD[3], BOARD[4], BOARD[5])
                wut(BOARD[6], BOARD[7], BOARD[8])
                wut(BOARD[0], BOARD[3], BOARD[6])
                wut(BOARD[1], BOARD[4], BOARD[7])
                wut(BOARD[2], BOARD[5], BOARD[8])
                wut(BOARD[0], BOARD[4], BOARD[8])
                wut(BOARD[2], BOARD[4], BOARD[6])
                if BR == 1:
                    WON = "WON"
                    ASP = 1
                    STARTCHOICE = ""
                    break
                if BOARD[0] in VAL and BOARD[1] in VAL and BOARD[2] in VAL and BOARD[3] in VAL and BOARD[4] in VAL and BOARD[5] in VAL and BOARD[6] in VAL and BOARD[7] in VAL and BOARD[8] in VAL:
                    WON = "WON"
                    WHO = "TIE"
                    ASP = 1
                    STARTCHOICE = ""
                    break
    if WON == "WON":
        #game stopped
        print
        graphicsboard(BOARD)
        print
        time.sleep(2)
        print
        if WHO == PLAYERNAME2:
            COMPUTERWINS = COMPUTERWINS + 1
        if WHO == PLAYERNAME:
            PLAYER1WINS = PLAYER1WINS + 1
        if WHO != "Error":
            if WHO == "TIE":
                print "Its a tie"
            else:
                print WHO, "won the game!"
            print
        RUNT = 1
        ANS = "Good"
        while ANS == "Good" and CR != "quit":
            MORE = raw_input("Do you want to contiue?: ").strip().lower()
            if MORE != "no" and MORE != "yes":
                print "You can only use yes or no to answer"
            if MORE == "yes":
                WON = "hur"
                ANS = "df"
                ASP = 1
            if MORE == "no":
                ALT = "done"
                ANS = "df"
print
print_slow("TicTacToe not running")
if RUNT == 1:
    time.sleep(2)
    print PLAYERNAME2, "have", COMPUTERWINS, "points"
    print PLAYERNAME, "have", PLAYER1WINS, "points"
    print ""
    time.sleep(1)
    if PLAYER1WINS == COMPUTERWINS:
        print "The game ended in a draw!"
    elif PLAYER1WINS > COMPUTERWINS:
        print PLAYERNAME, "won the game!"
    else:
        print PLAYERNAME2, "won the game!"
time.sleep(2)
print
print "Made by:"
print "Magnar Hole Polden"
print
time.sleep(5)
