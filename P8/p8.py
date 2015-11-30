#Programmer: Jordan Volk
#Date Written: October 27, 2015
#Program Name: P8.py
#Company Name: HTC-CCIS1505

lstNames = []

blnLoop = True #start loop
while blnLoop:
    strName = raw_input("Enter new student name or type QUIT to quit: ")
    tName = strName.title()
    
    if tName == "":
        print "Enter a valid input"
    else:
        if tName == "Quit":
            blnLoop = False
        else:
            lstNames.append(tName + "\n")

     
try:
    filNames = open("names.txt", "w") #open text file for read processing
    filNames.writelines(lstNames) #read data into a list
    filNames.close() #close file
except(IOError):
     print "Name file I/O error opening or writing"
     print "No other processing attempted"
     quit()

try:
    filNames = open("names.txt", "r")
    lstNames = filNames.readlines()
    filNames.close()
except(IOError):
    print "Name file I/O error opening or reading"
    print "No other processing attempted"
    quit()
lstNames.sort()
try:
    filNames = open("sortednames.txt", "w") 
    filNames.writelines(lstNames) 
    filNames.close()
except(IOError):
    print "Name file I/O error opening or writing"
    print "No other processing attempted"
    quit()
try:
    filNames = open("sortednames.txt", "r")
    lstNames = filNames.readlines()
    filNames.close()
except(IOError):
    print "Name file I/O error opening or reading"
    print "No other processing attempted"
    quit()

for names in lstNames:
    print names

#2
import cPickle

lstNums = []

blnLoop = True

while blnLoop:
    strNum = raw_input("Enter a number or type QUIT to quit: ")
    if strNum == "":
        print "Enter a valid input"

    else:
        tName = strNum.title()
        if tName == "Quit":
            blnLoop = False
        
        else:
            fltNum = float(strNum)
            lstNums.append(fltNum)


try:
    filNumbers = open("Numbers.dat", "w")
    cPickle.dump(lstNums, filNumbers)
    filNumbers.close()
except(IOError):
        print "Name file I/O error opening or writing"
        print "No other processing attempted"
        quit()
try:
    filNumbers = open("Numbers.dat", "r")
    lstNums = cPickle.load(filNumbers)
    lstNums.sort()
    filNumbers.close()    
except(IOError):
        print "Name file I/O error opening or reading"
        print "No other processing attempted"
        quit()
lstNums.sort()
try:
    filNumbers = open("SortedNumbers.dat", "w")
    cPickle.dump(lstNums, filNumbers)
    filNumbers.close()
except(IOError):
        print "Name file I/O error opening or writing"
        print "No other processing attempted"
        quit()
try:
    filNumbers = open("SortedNumbers.dat", "r")
    lstNums = cPickle.load(filNumbers)
    filNumbers.close()    
except(IOError):
        print "Name file I/O error opening or reading"
        print "No other processing attempted"
        quit()

for numbers in lstNums:
    print numbers

