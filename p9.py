#Programmer: Jordan Volk
#Date Written: November 17th, 2015
#Program Name: P9.py
#Company Name: HTC-CCIS1505



class Employee(object):
    """Employee class"""

    def __init__(self, Name="",Hours="", Rate=""): #constructor method
          self.EmployeeName = Name.title() #create employee name attribute
          self.EmployeeHours = Hours #create employee hours attribute
          self.EmployeeRate = Rate #create employee rate attribute
          print "*************************************************"
          print "Employee name is:", self.EmployeeName #accessing name attribute
          print "Employee's hours worked:", self.EmployeeHours #accessing Hours attribute
          print "Employee's hourly wage is:", self.EmployeeRate #accessing Rate attribute
          print "*************************************************"
    
    def __getEmpName(self):#get method to retrieve private/employee name
         strPW = raw_input("Enter access code to retrieve name: ")
         if strPW == "retrieve":
             return self.EmployeeName
         else:
             print "Access to Employee Name Denied!"

    def __setEmpName(self,EmpName=""): #set method to change or set private/employee name
        strPW = raw_input("Enter access code to change or update Employee name: ")
        if strPW == "update":
            self.EmployeeName = EmpName
            
        else:
            print "Incorrect access code, name not changed"
    EmpName = property(__getEmpName, __setEmpName)

    def Emppay(self): #method that calculates employee weekly pay
        if self.EmployeeHours <= 40:
            pay = self.EmployeeHours * self.EmployeeRate 
        
        else:
            pay = (self.EmployeeHours-40) * (self.EmployeeRate * float(1.5)) + (self.EmployeeRate * 40)
                       
        return pay           
                       
                       
                     
##########Mainline###########                   
strName = raw_input("Enter Employee name: ")
strHours = raw_input("Enter Hours worked: ")
intHours = int(strHours)
strRate = raw_input("Enter Hourly wage: ")
fltRate = float(strRate)
objEmployee = Employee(Name=strName, Hours=intHours, Rate=fltRate) #create an instance/object of Employee Class

strName = raw_input("Enter new name: ")
objEmployee.EmpName = strName #using property to set/change Name
print objEmployee.EmpName
pay = objEmployee.Emppay()
print "Employee Weekly pay is: ", pay

