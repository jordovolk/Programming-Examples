strName = raw_input("Enter your name: ")
intLen = len(strName)
print "Hi", strName.upper() + ", your name has", intLen, "characters in it,"
strLetter = raw_input("Enter a letter to search for: ")

if strLetter in strName:
    print "yes", strLetter
else:
    print "No", strLetter
