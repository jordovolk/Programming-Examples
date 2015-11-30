intTries = 0
strAnswer = "7"  #set lucky number
strGuess = ""
while strGuess != strAnswer:
    strGuess = raw_input("Guess the lucky number: ")
    intTries += 1  # add 1 to tries
print "Congrats, your guessed correctly"
print "It took you", intTries, "tries"
