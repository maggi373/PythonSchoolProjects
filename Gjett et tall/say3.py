# -*- coding: cp1252 -*-
import random
import time
runa=("yes","no")

print "Welcome to a guess game, were you guess the number that the computer has."
run = raw_input ("Start game?")
while run!="no":
    while run=="yes":
        x=random.randint(0, 10)
        a=raw_input("I have a number between 0 and 10, guess:")
        while a!=x:
            if a=="hack":
                print "The number is", x
                a=raw_input ("Type in number:")
            if a.lstrip("-").isdigit()==False:
                print "USE ONLY NUMBERS!"
                a=raw_input ("Try again:")
            if a.lstrip("-").isdigit()==True:
                a=int(a)
                if a!=x:
                    if a>x:
                        if a<=10:
                            print "The number has a lesser value"
                        else:
                            print "Too high number!"
                    if a<x:
                        if a>=0:
                            print "The number has a higher value"
                        else:
                            print "Too low number!"
                    a=raw_input ("Try again:")
        print "CORRECT!"
        run = raw_input ("Restart game?")
    while run not in runa:
        print "That is not an answear, please use yes or no to answear the question"
        run = raw_input ("Start game?")
if run=="no":
    print "game not running"
    time.sleep(2)
    print ""
    print ""
    print "Made by:"
    print "Magnar Hole Polden"
    time.sleep(10)

