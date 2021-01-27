# coding=UTF-8
"""
Fahrenheit - Celsius Calculator
VER 1.2

Made by
Magnar Hole Polden

"""

import time

CC = "c"
FF = "f"
RUN = "yes"

def error():
    """Error Message"""
    print
    print "You wrote something wrong, please try again"
    print "Write in the desired degree with the unit, eksample:"
    print "30c for celsius or 50f for fahrenheit"
    print "To quit just leave an blank field and press enter"

def calc(str1, str2):
    """Calculator"""
    global VALUE1
    stri = VALUE1.strip(str1)
    stri = float(str2)
    if str1 == "c":
        stri = stri*1.8+32
    if str1 == "f":
        stri = (stri-32)/1.8
    print str, str2

print "----- F-C CALC VER: 1.2 -----"
print
print "This is a Fahrenheit - Celsius Calculator"
print "Write in the desired degree with the unit, eksample: 30c or 50f"
print "To quit just leave an blank field and press enter"
while RUN == "yes":
    print
    VALUE1 = raw_input(": ").strip().lower()
    try:
        if VALUE1 == "":
            RUN = "no"
            break
        elif CC in VALUE1:
            calc("c", "Fahrenheit")
        elif FF in VALUE1:
            calc("f", "Celsius")
        else:
            error()
    except Exception:
        error()
if RUN == "no":
    print
    print "F-C CALC not running"
    print
    time.sleep(2)
    print
    print
    print "Made by:"
    print "Magnar Hole Polden"
    print
    time.sleep(10)
