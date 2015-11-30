class Student(object):
    """ HTC Student Class """

    GPA = 4.0 #class-level attribute
    def __init__(self, name = "", ID="", SSN=""): #constructor method
          self.StudentName = name.title() #create a student name attribute
          self.StudentID = ID #create student ID attribute
          self.__StudentSSN = SSN #create student SSN attribute/private attribute
          print "************************************"
          print "HTC student created!"
          print "Students name is:", self.StudentName #accessing name attribute
          print "Student ID is:", self.StudentID #accessing ID attribute
          print "Student GPA is:", self.GPA #accessing class-level attribute
          print "************************************"
    def Greeting(self): #method to greet
        print "Hello, I am an HTC student"

    def __getSSN(self): #get method to retrieve private SSN
        strPW = raw_input("Enter access code to retrieve SSN: ")
        if strPW == "dog":
            return self.__StudentSSN
        else:
            print "Access to SSN Denied"
    def __setSSN(self, SSN=""):
         strPW = raw_input("Enter access code to update SSN: ")
         if strPW == "monkey":
             self.__StudentSSN = SSN
            
         else:
            print "Incorrect access code, SSN not changed"
    SSN = property(__getSSN, __setSSN)   

####Mainline Code####
strName = raw_input("Enter student name: ")
strID = raw_input("Enter student ID: ")
strSSN = raw_input("Enter student SSN: ")
objStudent = Student(name=strName, ID=strID, SSN=strSSN) #create an instance/object of Student class
#objStudent.Greeting() #invoke Greeting method
print
#print objStudent.StudentName #access student name attribute (data)
#print objStudent.StudentID #access student ID attribute
#print objStudent.StudentGPA #access student GPA attribute

##print objStudent.getSSN() #get method
print objStudent.SSN #using property to retrieve SSN
strSSN = raw_input("Enter updated SSN: ")
objStudent.SSN = strSSN #using property to set/change SSN
##objStudent.setSSN(SSN=strSSN) #set method
print objStudent.SSN

