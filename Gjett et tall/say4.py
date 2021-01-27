# -*- coding: cp1252 -*-

#A simple guess me game
#Made by:
#Magnar Hole Polden

import random
#import random reg
import time
#imports time

runa=("yes","no")
#sets runa to have values yes and no
print "Welcome to a guess game, were you guess the number that the computer has."
#welcome text
run = raw_input ("Start game?")
#input for the user to set run

while run!="no":
    #loops as long run is not no
    while run=="yes":
        #loops as long run id is set as yes
        x=random.randint(0, 10)
        #make a random number between 0 and 10
        a=raw_input("I have a number between 0 and 10, guess:")
        #input for the user to guess a number        
        while a!=x:
            #loops as long the number is wrong
            if a=="hack":
                #cheat code
                print "The number is", x
                a=raw_input ("Type in number:")                
            if a.lstrip("-").isdigit()==False:
                #only use numbers code
                print "USE ONLY NUMBERS!"
                a=raw_input ("Try again:")                
            if a.lstrip("-").isdigit()==True:
                #supports negative numbers and positive numbers
                a=int(a)
                #translates from string to a variable
                if a!=x:
                    #must have
                    
                    if a>x:
                        #if a is bigger than x it does
                        if a<=10:
                            print "The number has a lesser value"
                        else:
                            print "Too high number!"
                            
                    if a<x:
                        #if a is smaller than x it does
                        if a>=0:
                            print "The number has a higher value"
                        else:
                            print "Too low number!"
                    a=raw_input ("Try again:")
                    #input for the user to try again                    
        print "CORRECT!"
        #if a is x then it prints correct!
        run = raw_input ("Restart game?")
        #user can choose to restart game        
    while run not in runa:
        #loops as long you dont type yes or no
        print "That is not an answear, please use yes or no to answear the question"
        run = raw_input ("Start game?")

if run=="no":
    #game stopped
    print "game not running"
    
    time.sleep(2)
    print ""
    print ""
    print "Made by:"
    print "Magnar Hole Polden"
    time.sleep(10)