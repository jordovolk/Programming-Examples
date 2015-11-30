strAnswer = "7"
blnDone = True
while blnDone:
    strGuess = raw_input("Guess the lucky number: ")
    if strGuess == strAnswer:
        blnDone = False
        print "You guessed correctly!"
        
