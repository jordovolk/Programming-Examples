# Programmer: Jordan Volk
# Date Written: September 22, 2015
# Program Name: P4.py
# Company Name: HTC-CCIS1505

#2
intLC = 1 
while intLC <= 10: 
    print "loop counter is:", intLC 
    intLC += 1
print "\n"
#3
intLC = 1
while intLC <= 101: 
    print "loop counter is:", intLC 
    intLC += 10
print "\n"
#4
intLc = 1000
while intLc >= 0: 
    print "loop counter is:", intLc 
    intLc -= 100
print "\n"

#5
strChoice = raw_input("Type a number between 1 & 10 for conversion to English: ") 
if strChoice == "1":
        print "One"
elif strChoice == "2":
        print "Two"
elif strChoice == "3":
        print "Three"
elif strChoice == "4":
        print "Four"
elif strChoice == "5":
        print "Five"
elif strChoice == "6":
        print "Six"
elif strChoice == "7":
        print "Seven"
elif strChoice == "8":
        print "Eight"
elif strChoice == "9":
        print "Nine"
elif strChoice == "10":
        print "Ten"
else:
    print("Error") #if number isnt found
print "\n"

#6
strName = "john doe"
strPW = "fopwpo"
blnDone = True
strNameinput = " "
strPWinput = " "

while blnDone:
    strNameinput = raw_input("Enter your username: ")
    strPWinput = raw_input("Enter your password: ")
    if strNameinput == strName and strPWinput == strPW:
        print "Login Successful"
        blnDone = False
    else:
        print"Error"


