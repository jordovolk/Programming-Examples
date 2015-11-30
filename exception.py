blnValid = False
while blnValid == False:
    try:
        intNum = int(raw_input("Enter a number: "))
        print intNum
        blnValid == True
    except(TypeError, ValueError), errMsg:
        print "you didn't enter a number"
        print errMsg
