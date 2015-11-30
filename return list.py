def getNames():
    """get names, append to list, return list"""
    blnGetNames = True
    lstNames = [ ] #empty list of names
    while blnGetNames:
        strName = raw_input("Enter a name, or press ENTER key to quit: ")
        
        if len(strName) > 0:
            lstNames.append(strName.title())
        else:
            blnGetNames = False
    return lstNames
####Mainline####
lstStudents = getNames()
print
print
print lstStudents
for student in lstStudents:
    print student
        
