# Programmer: Jordan Volk
# Date Written: October 13, 2015
# Program Name: P5.py
# Company Name: HTC-CCIS1505

#1
strWholeName = raw_input("Enter your first and last name: ")
print "Hi", strWholeName + ", your name has", len(strWholeName), "characters in it"
print
#2
tupMon = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemeber", "December",)
#3
for month in tupMon:
    print month[:3]
print
#4
for month in tupMon:
    if "J" in month[0]:
        print month[:3]
#5
print
strMonth = raw_input("Enter a month of the year ")
strMonth = strMonth.title()
if strMonth in tupMon:
    print "Month found"
else:
    print "Month not found"
print
#6
strName = raw_input("Enter your name ")
for strNumber in range(1, 11, 1):
    print strName, "loop counter = ", strNumber
print
#7
for strOdd in range(1,20,2):
    print strOdd




