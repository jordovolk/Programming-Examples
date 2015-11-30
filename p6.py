# Programmer: Jordan Volk
# Date Written: October 13, 2015
# Program Name: P6.py
# Company Name: HTC-CCIS1505

#1
lstWeek = []
intDayLoop =1
while intDayLoop <=7:
    strDay = raw_input("Enter each day of the week, one at a time: ")
    lstWeek.append(strDay.title())
    intDayLoop += 1
print
#2
for item in lstWeek:
    print item
#3
print
lstWeek.reverse()
for item in lstWeek:
    print item
#4
print
lstWeek.sort()
for item in lstWeek:
    print item
print
#5
for item in lstWeek:
    print item [:3]
print
#6
for item in lstWeek:
    if "T" in item[0]:
        print item
#7
print
dctCourses = {1000:"Intro to IS", 1505:"Fundamentals of Programming", 1515:"Web Programming Overview", 2575:".NET Programming 1",
              2585:".NET Programming 2", 2701:"Database Design & SQL"}
#8
lstValues = dctCourses.values()
lstValues.sort()
for item in lstValues:
    print item
print
#9
lstKey = dctCourses.keys()
lstKey.sort()
for item in lstKey:
    print item
print
#10
print dctCourses.get(1505)


