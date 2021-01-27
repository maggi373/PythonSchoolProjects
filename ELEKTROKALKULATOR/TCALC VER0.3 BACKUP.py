# coding=UTF-8
"""
Tcalc ver 0.3
An ohm's law calculator

Made by
Magnar Hole Polden

"""

#A simple calclulator
#Made by:
#Magnar Hole Polden

import random
#import random reg
import time
#imports time
import sys
import math

CHOICES = "volts", "ampere", "ohms", "wattage"
CVOLT = "volts"
CAMP = "ampere"
COHM = "Ohms"
CWATT = "Wattage"
RUNA = ("yes", "no")
#sets RUNA to have values yes and no

def cc(str5, str6, str7):
    if str5 in str6:
        str7 == str5

def print_slow(str0):
    """typing effect animation"""
    for letter in str0:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)
    print

def print_load(str1, str2, str3):
    """Loading animation"""
    for i in range(str1):
        print str3,
        time.sleep(str2)
    print

print_load(10, 0.1, ".")
#welcome text
RUN = raw_input("Start game?").strip().lower()
#input for the user to set RUN

while RUN not in RUNA:
    #loops as long you dont type yes or no
    print "That is not an answear, please use yes or no to answear the question"
    RUN = raw_input("Start game?").strip().lower()
    print ""
while RUN == "yes":
    print "What calclulation shall be calculated: Volt, Resistance, Ampere, Wattage"
    print "Please have:", CHOICES, "at the end of the number"
    CALC1 = raw_input("Value 1:").strip().lower()
    while CHOICES not in CALC1:
        print "Please have:", CHOICES, "at the end of the number"
        CALC1 = raw_input("Value 1:").strip().lower()
    if CALC1.lstrip(CHOICES).isdigit() == False:
        #only use numbers code
        print "ERROR"
        CALC1 = raw_input("Try again:")
    CALC2 = raw_input("Value 2:")
    while CHOICES not in CALC2:
        print "Please have:", CHOICES, "at the end of the number"
        CALC2 = raw_input("Value 2:").strip().lower()
    if CALC2.lstrip(CHOICES).isdigit() == False:
        #only use numbers code
        print "ERROR"
        CALC2 = raw_input("Try again:").strip().lower()

    CALCCHOICE = "Nothing"
    CALCCHOICE2 = "Nothing"
    cc(CVOLT, CALC1, CALCCHOICE)
    cc(CAMP, CALC1, CALCCHOICE)
    cc(COHM, CALC1, CALCCHOICE)
    cc(CWATT, CALC1, CALCCHOICE)
    cc(CVOLT, CALC2, CALCCHOICE2)
    cc(CAMP, CALC2, CALCCHOICE2)
    cc(COHM, CALC2, CALCCHOICE2)
    cc(CWATT, CALC2, CALCCHOICE2)

    if CALCCHOICE == CVOLT and CALCCHOICE2 == COHM:
        AMPS = VOLTS / RES
        WATTS = VOLTS ** 2 / RES
    if CALCCHOICE == CVOLT and CALCCHOICE2 == CAMP:
        OHMS = VOLTS / AMPS
        WATTS = VOLTS * AMPS
    if CALCCHOICE == CVOLT and CALCCHOICE2 == CWATT:
        AMPS = WATTS / VOLTS
        OHMS = VOLTS ** 2 / WATTS
    if CALCCHOICE == COHM and CALCCHOICE2 == CAMP:
        VOLTS = RES * AMPS
        WATTS = RES * AMPS ** 2
    if CALCCHOICE == COHM and CALCCHOICE2 == CWATT:
        VOLTS = math.sqrt(WATTS * RES)
        AMPS = math.sqrt(WATTS / RES)
    if CALCCHOICE == CAMP and CALCCHOICE2 == CWATT:
        VOLTS = WATTS / AMPS
        OHMS = WATSS / AMPS ** 2
    #something
    if CALCCHOICE2 == CVOLT and CALCCHOICE == COHM:
        AMPS = VOLTS / RES
        WATTS = VOLTS ** 2 / RES
    if CALCCHOICE2 == CVOLT and CALCCHOICE == CAMP:
        OHMS = VOLTS / AMPS
        WATTS = VOLTS * AMPS
    if CALCCHOICE2 == CVOLT and CALCCHOICE == CWATT:
        AMPS = WATTS / VOLTS
        OHMS = VOLTS ** 2 / WATTS
    if CALCCHOICE2 == COHM and CALCCHOICE == CAMP:
        VOLTS = RES * AMPS
        WATTS = RES * AMPS ** 2
    if CALCCHOICE2 == COHM and CALCCHOICE == CWATT:
        VOLTS = math.sqrt(WATTS * RES)
        AMPS = math.sqrt(WATTS / RES)
    if CALCCHOICE2 == CAMP and CALCCHOICE == CWATT:
        VOLTS = WATTS / AMPS
        OHMS = WATSS / AMPS ** 2
    print "Volt:", VOLTS
    print "Ampere", AMPS
    print "Ohms:", OHMS
    print "Watts", WATTS
    

if RUN == "no":
    #game stopped
    print ""
    print_slow("game not running")
    print ""
    time.sleep(2)
    print ""
    print ""
    print "Made by:"
    print "Magnar Hole Polden"
    print ""
    time.sleep(10)
