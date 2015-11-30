def Input():
    """Get users first and last name
        concatentate FN an LN
        return full name
    """
    strFName = raw_input("Enter your first name: ")
    strLName = raw_input("Enter your last name: ")
    strFullName = strFName + " " + strLName
    return strFullName

def Process(name):
    strNameT = name.title()
    return strNameT

def Output(name):
    print "Hello", name, "have a nice day!"
########Mainline
strUserName = Input()
#print strUserName.title()
strUserNameT = Process(strUserName)
Output(strUserNameT)
