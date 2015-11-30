import cPickle

filStudents = open("students.txt", "r")
lstStudents = filStudents.readlines()
filStudents.close()

filStudents = open("students.dat", "w")
cPickle.dump(lstStudents, filStudents)
filStudents.close()

filStudents = open("students.dat", "r")
lstStudents = cPickle.load(filStudents)
filStudents.close()
print lstStudents
