import cPickle
lstNums = [33,66.25,44,11,99.33,22,"jordan"]
filNums = open("numbers.dat", "w")
cPickle.dump(lstNums, filNums)
filNums.close()
