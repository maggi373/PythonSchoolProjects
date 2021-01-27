import time
end1="program not running"
end2="I think we need to have a divorce"
end3="Good bye to you sir!"
run = raw_input ("run program?")
         
while run=="yes":
    c = input ("1=+, 2=-, 3=*, 4=/")
    a = input ("ATAT value")
    b = input ("Bass value")
    if c==1:
        print a,"+",b,"=", a+b
    if c==2:
        print a,"-",b,"=", a-b
    if c==3:
        print a,"*",b,"=", a*b
    if c==4:
        print a,"/",b,"=", a/b
    run = raw_input ("run program again?")


if run=="no":
    print end1
    time.sleep(2)
    print end2
    time.sleep(3)
    print end3

else:
    print "That is not an answear, please use yes or no to answear the question"
    run = raw_input ("run program?")



