#Programmer: Jordan Volk
#Date Written: November 23rd, 2015
#Program Name: P10.py
#Company Name: HTC-CCIS1505

class ChkAcct(object):
    """Checking Account class"""

    def __init__(self, dollars=0): #constructor method
        self.__CBalance = float(dollars) #create private checking balance attribute
        print "Checking account created"
        print "Beginning Checking Account Balance:", self.__CBalance

    def __getCBalance(self): #get method for private Inventory attribute
        return self.__CBalance
    def __setCBalance(self,dollars=0): #set method for private inventory attribute
        self.__CBalance = float(dollars)
    CBalance = property(__getCBalance, __setCBalance)

    def Deposit(self, dollars=0): #deposit into checking method
        self.CBalance += float(dollars)
    def Withdraw(self, dollars=0): #withdraw from checking method
        self.CBalance -= float(dollars)
    def Xfer(self, dollars=0, SavAcct=None): #checking to savings transfer
        self.CBalance -= float(dollars)
        SavAcct.Deposit(dollars=dollars)

class SavAcct(object):
    """Savings account class"""

    def __init__(self, dollars=0): #constructor method
         self.__SBalance = float(dollars) #create private checking balance attribute
         print "Savings account created"
         print "Beginning Savings Account Balance:", self.__SBalance

    def __getSBalance(self): #get method for private Inventory attribute
        return self.__SBalance
    def __setSBalance(self,dollars=0): #set method for private inventory attribute
        self.__SBalance = float(dollars)
    SBalance = property(__getSBalance, __setSBalance)

    def Deposit(self, dollars=0): #deposit into savings method
        self.SBalance += float(dollars)
    def Withdraw(self, dollars=0): #withdraw from savings method
        self.SBalance -= float(dollars)
    def Xfer(self, dollars=0, ChkAcct=None): #Savings to Checking transfer
        self.SBalance -= float(dollars)
        ChkAcct.Deposit(dollars=dollars)

    
########Mainline#########
strCBalance = raw_input("Enter beginning Checking account Balance: ")
strSBalance = raw_input("Enter beginning Savings account Balance: ")
print
objChkAcct = ChkAcct(dollars=strCBalance) #create Chking object/instance
print
objSavAcct = SavAcct(dollars=strSBalance) #create Saving object/instance


strDepositSavings = raw_input("Enter an amount you wish to deposit into Savings: ")
objSavAcct.Deposit(dollars=strDepositSavings)
print "Updated Savings Balance:", objSavAcct.SBalance
print
strDepositChecking = raw_input("Enter an amount you wish to deposit into Checking: ")
objChkAcct.Deposit(dollars=strDepositChecking)
print "Updated Checking Balance:", objChkAcct.CBalance
print
strWithdrawSavings = raw_input("Enter an amount you wish to withdraw from Savings: ")
objSavAcct.Withdraw(dollars=strWithdrawSavings)
print "Updated Savings Balance:", objSavAcct.SBalance
print
strWithdrawChecking = raw_input("Enter an amount you wish to withdraw from Checking: ")
objChkAcct.Withdraw(dollars=strWithdrawChecking)
print "Updated Checking Balance:", objChkAcct.CBalance
print
strXferS = raw_input("How much would you like to transfer from checking to savings account?: ")
objSavAcct.Deposit(dollars=strXferS)
objChkAcct.Withdraw(dollars=strXferS)
print "Savings Updated Balance after transfer:", objSavAcct.SBalance
print "Checking Updated Balance after transfer:", objChkAcct.CBalance
print
strXferC = raw_input("How much would you like to transfer from savings to Checking account?: ")
objSavAcct.Withdraw(dollars=strXferC)
objChkAcct.Deposit(dollars=strXferC)
print "Savings Updated Balance after transfer:", objSavAcct.SBalance
print "Checking Updated Balance after transfer:", objChkAcct.CBalance
