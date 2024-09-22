worldDb ={
          "England":"London",
          "India":"New Delhi",
          "China":"Beijing"
}

quit= False

while not quit:
    Option=input("What would you like to do?\n\n1. Insert into database\n2. Display all countries\n3. Display all capitals\n4. Delete from database\n5. Retrieve Capital\n6. Quit\n\n")    
    """while Option not in ['1','2','3','4','5', '6']:
        print("Invalid input. Please try again.")
        Option=input("\nWhat would you like to do?\n\n1. Insert into database\n2. Display all countries\n3. Display all capitals\n4. Delete from database\n5. Retrieve Capital6. Quit\n\n")"""
    if Option=='1':
        countryinput=input("Enter country name: ")
        capitalinput=input("Enter capital name: ")
        if countryinput in worldDb:
            print("Country already in database")
        else:
            worldDb[countryinput]=capitalinput
            print('Entered')
            print(worldDb)

    elif Option=='2':
        print(worldDb.keys())
    elif Option=="3":
        print(worldDb.values())
    elif Option=='4':
        delinput= input('Which country would you like to delete from the database?\n')
        if delinput in worldDb:
            del(worldDb[delinput])
        else:
            print('Not in database')
    elif Option=="5":
        
        capitalfind= input('Which country would you like to know the country of?\n')
        if capitalfind in worldDb:
            print(worldDb[capitalfind])
        else:
            print('Not in database')
    elif Option=="6":
        quit=True
    else:
        print('Invalid input.')