firstName=raw_input("enter your first name")
lastName=raw_input("enter your last name")
if firstName == "":
 print "you didn't enter a first name"
if lastName == "":
    print "you didn't enter a last name"
    print "Unable to process!"
else:
    fullName=firstName + lastName
    nameLen=len(fullName)
    print "your name is " + str(nameLen) + " characters long"
    for letter in fullName:
        print letter
