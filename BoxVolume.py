def BV(L=1, W=1, H=1):
    """calculates box volume based on length, width and height"""
    volume = int(L) * int(W) * int(H)
    return volume

####mainline####
##print BV()
##print BV(L=10)
##print BV(L=10, W=3)
##print BV(L=10, W=3, H=5)
##print BV(H=5, W=3, L=10)
##print BV(H=5, W=3)
strL= raw_input("Enter box length: ")
strW= raw_input("Enter box width: ")
strH= raw_input("Enter box height: ")

intVolume = BV(L=strL, W=strW, H=strH)
print intVolume

