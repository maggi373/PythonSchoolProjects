# coding=UTF-8
"""
Tcalc ver 1.7
An ohm's law calculator

Made by
Magnar Hole Polden

"""

import time
import sys
import math

CHOICES = ("volts", "amps", "ohms", "watts")
CVOLT = "volts"
CAMP = "amps"
COHM = "ohms"
CWATT = "watts"
CALC1 = "0"
CALC11 = 0
CALC2 = "0"
CALC21 = 0
CALCCHOICE = "0"
CALCCHOICE2 = "0"
ERROR = "O"

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

print "----- TCALC -----"
print
print_load(5, 0.1, ".")
print_slow("Tcalc VER: 1.7")
RUN = "yes"
while RUN != "no":
    VOLTS = "0"
    AMPS = "0"
    OHMS = "0"
    WATTS = "0"
    ERROR = "O"
    CALC1 = "0"
    CALC2 = "0"
    ERRORC = 0
    print "Provide two values, and I will calculate the two missing values"
    print "Please have either of:", CHOICES, "at the end of the number"
    CALC1 = raw_input("Value 1: ").strip().lower()
    if CALC1 == "":
        RUN = "no"
        break
    elif CVOLT in CALC1:
        CALCCHOICE = CVOLT
        CALC11 = CALC1.strip(CVOLT)
    elif CAMP in CALC1:
        CALCCHOICE = CAMP
        CALC11 = CALC1.strip(CAMP)
    elif COHM in CALC1:
        CALCCHOICE = COHM
        CALC11 = CALC1.strip(COHM)
    elif CWATT in CALC1:
        CALCCHOICE = CWATT
        CALC11 = CALC1.strip(CWATT)
    else:
        ERROR = "E"
        ERRORC = 1
    if ERROR == "O":
        try:
            CALC11 = float(CALC11)
        except Exception:
            ERROR = "E"
            ERRORC = 1
    if ERROR == "O":
        CALC2 = raw_input("Value 2: ").strip().lower()
        if CALC2 == "":
            RUN = "no"
            break
        elif CVOLT in CALC2:
            CALCCHOICE2 = CVOLT
            CALC21 = CALC2.strip(CVOLT)
        elif CAMP in CALC2:
            CALCCHOICE2 = CAMP
            CALC21 = CALC2.strip(CAMP)
        elif COHM in CALC2:
            CALCCHOICE2 = COHM
            CALC21 = CALC2.strip(COHM)
        elif CWATT in CALC2:
            CALCCHOICE2 = CWATT
            CALC21 = CALC2.strip(CWATT)
        else:
            ERROR = "E"
            ERRORC = 2
    if ERROR == "O":
        try:
            CALC21 = float(CALC21)
        except Exception:
            ERROR = "E"
            ERRORC = 2
    if CALC11 != 0 and CALC21 != 0 and ERROR == "O":
        if CVOLT in CALCCHOICE and COHM in CALCCHOICE2:
            AMPS = CALC11 / CALC21
            WATTS = CALC11 ** 2 / CALC21
        elif CVOLT in CALCCHOICE and CAMP in CALCCHOICE2:
            OHMS = CALC11 / CALC21
            WATTS = CALC11 * CALC21
        elif CVOLT in CALCCHOICE and CWATT in CALCCHOICE2:
            AMPS = CALC21 / CALC11
            OHMS = CALC11 ** 2 / CALC21
        elif COHM in CALCCHOICE and CAMP in CALCCHOICE2:
            VOLTS = CALC11 * CALC21
            WATTS = CALC11 * CALC21 ** 2
        elif COHM in CALCCHOICE and CWATT in CALCCHOICE2:
            VOLTS = math.sqrt(CALC11 * CALC21)
            AMPS = math.sqrt(CALC21 / CALC11)
        elif CAMP in CALCCHOICE and CWATT in CALCCHOICE2:
            VOLTS = CALC21 / CALC11
            OHMS = CALC21 / CALC11 ** 2
        elif CVOLT in CALCCHOICE2 and COHM in CALCCHOICE:
            AMPS = CALC21 / CALC11
            WATTS = CALC21 ** 2 / CALC11
        elif CVOLT in CALCCHOICE2 and CAMP in CALCCHOICE:
            OHMS = CALC21 / CALC11
            WATTS = CALC21 * CALC11
        elif CVOLT in CALCCHOICE2 and CWATT in CALCCHOICE:
            AMPS = CALC11 / CALC21
            OHMS = CALC21 ** 2 / CALC11
        elif COHM in CALCCHOICE2 and CAMP in CALCCHOICE:
            VOLTS = CALC21 * CALC11
            WATTS = CALC21 * CALC11 ** 2
        elif COHM in CALCCHOICE2 and CWATT in CALCCHOICE:
            VOLTS = math.sqrt(CALC11 * CALC21)
            AMPS = math.sqrt(CALC21 / CALC11)
        elif CAMP in CALCCHOICE2 and CWATT in CALCCHOICE:
            VOLTS = CALC11 / CALC21
            OHMS = CALC11 / CALC21 ** 2
        print
        if CVOLT in CALC1:
            print CALC11, "V"
        elif CVOLT in CALC2:
            print CALC21, "V"
        else:
            print VOLTS, "V"
        print
        if CAMP in CALC1:
            print CALC11, "A"
        elif CAMP in CALC2:
            print CALC21, "A"
        else:
            print AMPS, "A"
        print
        if COHM in CALC1:
            print CALC11, "Ω"
        elif COHM in CALC2:
            print CALC21, "Ω"
        else:
            print OHMS, "Ω"
        print
        if CWATT in CALC1:
            print CALC11, "W"
        elif CWATT in CALC2:
            print  CALC21, "W"
        else:
            print WATTS, "W"
        print
    else:
        print "You wrote something wrong!"
        if ERRORC == 0:
            print "The value of Value 1:", CALC1
            print "The value of Value 2:", CALC2
        elif ERRORC == 1:
            print "The value of Value 1 is wrong, you typed:", CALC1
        elif ERRORC == 2:
            print "The value of Value 2 is wrong, you typed:", CALC2
        print "The correct way to write is; [number] [suffix]"
        print
if RUN == "no":
    print
    print_slow("Tcalc not running")
    print
    time.sleep(2)
    print
    print
    print "Made by:"
    print "Magnar Hole Polden"
    print
    time.sleep(10)
