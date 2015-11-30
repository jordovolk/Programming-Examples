

try:
    filStudents = open("students.txt", "r") #open text file for read processing
    lstStudents = filStudents.readlines() #read data into a list
    filStudents.close() #close file
except(IOError):
    print "Student file I/O error opening or reading"
    print "no other processing was done"
    quit()



#print lstStudents
##print
##for student in lstStudents:
##    print student.title()

strStudent = raw_input("Enter new student name: ")
if len(strStudent) > 0:
    lstStudents.append(strStudent.lower() + "\n") #add new student to the list

lstStudents.sort() #sort students

filStudents = open("sortedstudents.txt", "w")
filStudents.writelines(lstStudents)
filStudents.close()
