blnDone = False
while blnDone == False:
    print \
    """
    Steve's Diner Breakfast Choices:
    1) Eggs & Toast
    2) Pancakes
    3) French Toast
    4) Omlette
    5) Oatmeal

    """

    strChoice = raw_input("What do you want for breakfast: ")

    if strChoice == "1":
        print "Enjoy your Eggs & Toast"
        blnDone = True
    elif strChoice == "2":
        print "Enjoy your Pancakes"
        blnDone = True
    elif strChoice == "3":
        print "Enjoy your French Toast"
        blnDone = True
    elif strChoice == "4":
        print "Enjoy your Omlette"
        blnDone = True
    elif strChoice == "5":
        print "Enjoy your Oatmeal"
        blnDone = True
    else:
        print "You didn't choose a valid menu item"
        print "You will starve"











    















