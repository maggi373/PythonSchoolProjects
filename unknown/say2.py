# -*- coding: cp1252 -*-
import random
import time
runa=("yes","no")

print "Welcome to a guess game, were you guess the number that the computer has."
run = raw_input ("Start game?")
while run!="no":
    while run=="yes":
        x=random.randint(0, 10)
        a=raw_input("Har et tall mellom 0-10, gjett:")
        while x!=a:
            while a.isdigit():
                a=int(a)
                while a>10 or a<0:
                    if a>10:
                        print "Tallet er høgere enn 10"
                    if a<0:
                        print "Tallet er lavere enn 0"
                    a=raw_input ("prøv igjen:")
                if a>x:
                    print "Tallet er mindre"
                if a<x:
                    print "tallet er større"
                a=raw_input ("prøv igjen:")
        else:
            print "Use numbers!"
            a=raw_input ("prøv igjen:")
        print "riktig"
        run = raw_input ("run program again?")
    if run!=runa:
        print "That is not an answear, please use yes or no to answear the question"
        run = raw_input ("run program?")
if run=="no":
    print "program not running"
    time.sleep(2)
    print "I think we need to have a divorce"
    time.sleep(3)
    print "Good bye to you sir!"
    time.sleep(4)

