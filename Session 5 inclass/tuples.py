tupStudents = ("ron", "jordan", "joe", "bob", "sue")
print tupStudents
print
for student in tupStudents:
    print student
print
strName = raw_input("Enter student to search for: ")
if strName.lower() in tupStudents:
    print "yes"
else:
    print "No"
print
print "There are", len(tupStudents)," students in the class"
print
print tupStudents[1]
print
print tupStudents[1:4]
