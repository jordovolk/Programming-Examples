#Programmer: Jordan Volk
#Date Written: October 20, 2015
#Program Name: P7.py
#Company Name: HTC-CCIS1505
#1
def Input():
    """Get users first and last name
        concatentate FN an LN
        return full name
    """
    strFullName = raw_input("Please enter your full name: ") #get name
    return strFullName #return name to Format()
     

def Format(Name): #call strFullName
    strNameT = Name.title() #turn to title format
    return strNameT #return strNameT to Greeting()
    

def Greeting(Name):
    print "Hello " + Name + "." #get formatted name and add greeting
 
#2

def List():
    lstScore = [] #create empty list

    blnLoop = True #start loop
    while blnLoop:
        strScore = raw_input("Enter a score or press ENTER to quit: ") #get input
        if strScore == "": #stop loop if empty string
            blnLoop = False #ends loop
        else:
            lstScore.append(int(strScore)) #add to list
    return lstScore #gives list to all other functions

def Average(List):
     lstTotal = 0
     for item in List:
         lstTotal += item #add next item in list to total
     lstAverage = lstTotal/len(List) #divide total by list length
     return lstAverage #return average score

def Min(List):
    List.sort()
    return List[0] #return smallest score

def Max(List):
    List.sort()
    List.reverse()
    return List[0] #return largest score

def Output(Minimum,Maximum,Average):
    print "The Minimum score was",Minimum
    print "The Maximum score was",Maximum
    print "The Average score was",Average

#3
def BV():
    strLength = raw_input("Enter box length: ")
    strWidth = raw_input("Enter box width: ")
    strHeight = raw_input("Enter box height: ")
    volume = float(strLength)*float(strWidth)*float(strHeight) #finds volume and converts to float
    print
    print "The volume of one box is",volume,"units" #print volume of box
    return volume

def TotalVolume(Volume):
    strBoxQty = raw_input("How many boxes do you have? ") #how many boxes are there
    intBoxQty = int(strBoxQty)
    intTotalVolume = Volume*intBoxQty #take volume of one box and multiply
    return intTotalVolume
def OutputVolume(TotalVolume):
    print "You will need",str(TotalVolume),"cubic units to store these boxes."



######Mainline
strUserName = Input()
strUserNameT = Format(strUserName)
Greeting (strUserNameT)
print

intScoreList = List()
intAverage = Average(intScoreList)
intMin = Min(intScoreList)
intMax = Max(intScoreList)
Output(intMin,intMax,intAverage)
print

intVolume = BV()
intTotalVolume = TotalVolume(intVolume)
OutputVolume(intTotalVolume)
