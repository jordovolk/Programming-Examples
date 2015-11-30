# Programmer: Jordan Volk
# Date Written: September 1, 2015
# Program Name: Program3.py
# Company Name: HTC-CCIS1505
print"\"Hi, my name is Jordan!\", said Jordan. "

strName = raw_input("What is your name? ")

print("Hi " + strName + ", nice to meet you. ")
print "I'm 18.",
Age = raw_input("How old are you? ")

intTransform = int(Age)

calculation = intTransform * 365 * 24 * 60 * 60

print("Hi " + strName + ", did you know you are " + str(calculation) + " seconds old")

print "\n"

strFavNumber = raw_input("What's your favorite number? ")

intFavNumber= int(strFavNumber)

strFavCalc = intFavNumber * 2

print("Your favorite number doubled = " + str(strFavCalc))

print "\n"

print "130/10 (as float)=", 130/10.0
print "233/3.3 (as float)=", 233/3.3
print "233 / 3 (as an integer) is", 233/3
print "The remainder of 233 / 3 is", 233%3
print "2 to the power of 32 =", 2**32
print "((456.782/45.1)-78.9) (as float)=", ((456.782/45.1)-78.9)

print "\n"

print "Thank you for answering my questions " + strName + ",",
print "have a good day."
