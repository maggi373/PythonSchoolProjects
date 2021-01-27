"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""

# -*- coding: cp1252 -*-

#A simple calclulator
#Made by:
#Magnar Hole Polden

import time
#imports time
import sys
import math

CHOICES = ("volts", "amps", "ohms", "watts,")
CHOICES2 = ("volts", "amps", "ohms", "watts", "quit")
CVOLT = ("volts")
CAMP = ("amps")
COHM = ("ohms")
CWATT = ("watts")
RUNA = ("yes", "no")
CALC1 = ("0")
CALC11 = (0)
CALC2 = ("0")
CALC21 = (0)
CALCCHOICE = "0"
CALCCHOICE2 = "0"

#sets RUNA to have values yes and no

def ccu(str5, str6, str7):
    """if something stuff"""
    if str5 in str6:
        str5[0] = str7

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

def preprocess(str8):
    """String and lowercase the input."""
    return str8.strip().lower()



print "This program is in alpha, there are many bugs"
print_load(10, 0.1, ".")
print_slow("Tcalc VER: 1.3")
#welcome text
RUN = raw_input("Start Tcalc?")
preprocess(RUN)
#input for the user to set RUN
while RUN != "no":
    VOLTS = 0
    AMPS = 0
    OHMS = 0
    WATTS = 0
    while RUN not in RUNA:
        #loops as long you dont type yes or no
        print "That is not an answer, please use yes or no to answear the question"
        RUN = raw_input("Start Tcalc?")
        preprocess(RUN)
        print ""
    print "What calclulation shall be calculated: Volt, Resistance, Ampere, Wattage"
    print "Please have:", CHOICES, "at the end of the number"
    CALC1 = raw_input("Value 1:")
    if CALC1 == "":
        RUN = "no"
        break
    if CVOLT in CALC1:
        CALCCHOICE = CVOLT
        CALC11 = CALC1.strip(CVOLT)
    if CAMP in CALC1:
        CALCCHOICE = CAMP
        CALC11 = CALC1.strip(CAMP)
    if COHM in CALC1:
        CALCCHOICE = COHM
        CALC11 = CALC1.strip(COHM)
    if CWATT in CALC1:
        CALCCHOICE = CWATT
        CALC11 = CALC1.strip(CWATT)
    CALC2 = raw_input("Value 2:")
    if CALC2 == "":
        RUN = "no"
        break
    if CVOLT in CALC2:
        CALCCHOICE2 = CVOLT
        CALC21 = CALC2.strip(CVOLT)
    if CAMP in CALC2:
        CALCCHOICE2 = CAMP
        CALC21 = CALC2.strip(CAMP)
    if COHM in CALC2:
        CALCCHOICE2 = COHM
        CALC21 = CALC2.strip(COHM)
    if CWATT in CALC2:
        CALCCHOICE2 = CWATT
        CALC21 = CALC2.strip(CWATT)
    CALC11 = int(CALC11)
    CALC21 = int(CALC21)

    if CVOLT in CALCCHOICE and COHM in CALCCHOICE2:
        AMPS = CALC11 / CALC21
        WATTS = CALC11 ** 2 / CALC21
    if CVOLT in CALCCHOICE and CAMP in CALCCHOICE2:
        OHMS = CALC11 / CALC21
        WATTS = CALC11 * CALC21
    if CVOLT in CALCCHOICE and CWATT in CALCCHOICE2:
        AMPS = CALC21 / CALC11
        OHMS = CALC11 ** 2 / CALC21
    if COHM in CALCCHOICE and CAMP in CALCCHOICE2:
        VOLTS = CALC11 * CALC21
        WATTS = CALC11 * CALC21 ** 2
    if COHM in CALCCHOICE and CWATT in CALCCHOICE2:
        VOLTS = math.sqrt(CALC11 * CALC21)
        AMPS = math.sqrt(CALC21 / CALC11)
    if CAMP in CALCCHOICE and CWATT in CALCCHOICE2:
        VOLTS = CALC21 / CALC11
        OHMS = CALC21 / CALC11 ** 2
    if CVOLT in CALCCHOICE2 and COHM in CALCCHOICE:
        AMPS = CALC21 / CALC11
        WATTS = CALC21 ** 2 / CALC11
    if CVOLT in CALCCHOICE2 and CAMP in CALCCHOICE:
        OHMS = CALC21 / CALC11
        WATTS = CALC21 * CALC11
    if CVOLT in CALCCHOICE2 and CWATT in CALCCHOICE:
        AMPS = CALC11 / CALC21
        OHMS = CALC21 ** 2 / CALC11
    if COHM in CALCCHOICE2 and CAMP in CALCCHOICE:
        VOLTS = CALC21 * CALC11
        WATTS = CALC21 * CALC11 ** 2
    if COHM in CALCCHOICE2 and CWATT in CALCCHOICE:
        VOLTS = math.sqrt(CALC11 * CALC21)
        AMPS = math.sqrt(CALC21 / CALC11)
    if CAMP in CALCCHOICE2 and CWATT in CALCCHOICE:
        VOLTS = CALC11 / CALC21
        OHMS = CALC11 / CALC21 ** 2

    print
    if CVOLT in CALC1:
        print "Volt:", CALC11
    elif CVOLT in CALC2:
        print "Volt:", CALC21
    else:
        print "Volt:", VOLTS
    print
    if CAMP in CALC1:
        print "Ampere:", CALC11
    elif CAMP in CALC2:
        print "Ampere:", CALC21
    else:
        print "Ampere:", AMPS
    print
    if COHM in CALC1:
        print "Ohms:", CALC11
    elif COHM in CALC2:
        print "Ohms:", CALC21
    else:
        print "Ohms:", OHMS
    print
    if CWATT in CALC1:
        print "Watts:", CALC11
    elif CWATT in CALC2:
        print "Watts:", CALC21
    else:
        print "Watts:", WATTS
    print

if RUN == "no":
    #game stopped
    print ""
    print_slow("Tcalc not running")
    print ""
    time.sleep(2)
    print ""
    print ""
    print "Made by:"
    print "Magnar Hole Polden"
    print ""
    time.sleep(10)
