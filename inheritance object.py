class Facility(object):#HTC phones base class
    def __init__(self, ID="", LOC="", items=0):
        self.ID = ID #create store ID public attribute
        self.Location = LOC #create store location public attribute
        try:
            self.__Inventory = int(items) #create store inventory private attribute
        except:
            print "Invalid inventory entered - defaulting to (0)"
            self.__Inventory = 0
        print "HTC Facility created"
        if ID[0].lower() == "s"
            print "Store:", self.ID
        else:
            print "Warehouse:", self.ID
        print "Inventory:", self.__Inventory
        print "Location:", self.Location

    def __getInv(self): #get method for private Inventory attribute
        return self.__Inventory
    def __setInv(self,items=0): #set method for private inventory attribute
        self.__Inventory = int(items)
    inventory = property(__getInv, __setInv)
    def Receive(self, items=0): #receive from warehouse method
        self.inventory += int(items)
    
class Store(Facility):
    """HTC Phones Store class to sell mobile phones"""
    def Sale(self, items=0): #sale method
        self.inventory -= int(items) #use property

    def Return(self, items=0): #Customer return method
        self.inventory += int(items)

    def Xfer(self, items=0, whse=None):
        self.inventory -= int(items) #deplete store inventory
        whse.Receive(items=items)

class Warehouse(Facility):
    """HTC Phones Warehouse class to sell mobile phones"""
    def Ship(self, items=0): #Ship method
        self.inventory -= int(items) #use property

    def Return(self, items=0): #Warehouse return to supplier/vendor method
        self.inventory -= int(items)

    def Receive(self, items=0): #Customer receive method
        self.inventory += int(items)
    def Xfer(self, items=0, store=None): #Whse to store transfer
        self.inventory -= int(items)
        store.Receive(items=items)

############Mainline##############
strID = raw_input("Enter store ID: ")
strLoc = raw_input("Enter store Location(Zipcode): ")
strInv = raw_input("Enter store beginning Inventory: ")
print
objStore = Store(ID=strID,LOC=strLoc,items=strInv) #create store object/instance
print
print objStore.inventory #accessing inventory using property
strInv = raw_input("Enter store updated Inventory: ")
objStore.inventory = strInv #update inventory using property
print objStore.inventory

strItems = raw_input("Enter number of phones being sold: ")
objStore.Sale(items=strItems)
print "Store Inventory:", objStore.inventory
print
strItems = raw_input("Enter number of customer phones being returned: ")
objStore.Return(items=strItems)
print "Store Inventory:", objStore.inventory
print
strItems = raw_input("Enter number of customer phones being received from warehouse: ")
objStore.Receive(items=strItems)
print "Store Inventory:", objStore.inventory
strID = raw_input("Enter Warehouse ID: ")
strLoc = raw_input("Enter Warehouse Location(Zipcode): ")
strInv = raw_input("Enter Warehouse beginning Inventory: ")
print
objWhse = Warehouse(ID=strID,LOC=strLoc,items=strInv) #create warehouse object/instance
strItems = raw_input("Enter number of phones being shipped to store: ")
objWhse.Ship(items=strItems)
print "Warehouse Inventory:", objWhse.inventory
print
strItems = raw_input("Enter number of phones being returned to supplier: ")
objWhse.Return(items=strItems)
print "Warehouse Inventory:", objWhse.inventory
print
strItems = raw_input("Enter number of phones being received from supplier: ")
objWhse.Receive(items=strItems)
print "Warehouse Inventory:", objWhse.inventory
print
print
strItems = raw_input("Enter number of phones to transfer from store to warehouse: ")
objStore.Xfer(items=strItems, whse=objWhse)
print "Store Inventory:", objStore.inventory
print "Warehouse Inventory:", objWhse.inventory
print
print
strItems = raw_input("Enter number of phones to transfer from warehouse to store: ")
objWhse.Xfer(items=strItems, store=objStore)
print "Store Inventory:", objStore.inventory
print "Warehouse Inventory:", objWhse.inventory




