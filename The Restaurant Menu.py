def createMenu():
    """
    This function add new item to the Menu.
    """
    global menuDic
    wantscontinue = True

    while wantscontinue:
        key = input("Please type a new menu item:")
        # checking the input string?

        try:
            value = float(input("Please type the price of the item:"))
        except:
            print("Invalid entry!")
            break
        # check the valid entry (float)

        menuDic[key] = value
        print(printMenu(menuDic))

        choice = input("Do you want to add one more item? Please type 'yes' or 'no'.")
        # check yes or no
        if choice == "yes":
            continue
        elif choice == "no":
            wantscontinue = False


def printMenu(menuDic):
    """
    This function print the Menu in a beter way.
    """
    max_length = max(len(key) + len(str(value)) for key, value in menuDic.items())
    theText = " MENU ".center((max_length + 2), "*")
    for key, value in menuDic.items():
        theText += (
            f"\n{key}{'-' * (max_length - len(key) - len(str(value)) + 2)}{value}"
        )
    return theText


def deleteAnItem():
    """
    This function delete an item from the Menu.
    """
    # global menuDic
    whichOne = input("Which item do you want to delete from MENU items?")
    try:
        del menuDic[whichOne]
    except:
        print("Invalid Entry. \nHere is ")
    print(printMenu(menuDic))


def changetheprice():
    """
    This function change the price of an item in the Menu.
    """
    name = input("What do you want to change the price of?")
    if name in menuDic.keys():
        try:
            new_price = float(input("What is the new price?"))
            menuDic[name] = new_price
        except:
            print("Please enter valid entry like numbers!")
    else:
        print(f"There is no item in the menu like {name}. /nPlease try again!")
    print(printMenu(menuDic))


def saveMenu():
    """
    This function save the Menu in an external file.
    """
    # theMenuText = printMenu(menuDic)
    # f = open("TheMenu.txt", "w")
    # f.write(theMenuText)
    # f.close()
    # print("The menu is saved as 'TheMenu.txt'")

    theMenuText = printMenu(menuDic)
    with open("TheMenu.txt", "w") as file:
        file.write(theMenuText)
    print("The menu is saved as 'TheMenu.txt'")
    # File is closed automatically thankfullly "with" statement.


menuDic = {
    "Sandwich": 10.0,
    "Apple": 5.0,
    "Sinasappel": 6.0,
    "Chips": 4.0,
    "Cheese": 3.5,
    "Chocolate": 8.0,
}
user_wants_continue = True

while user_wants_continue:
    """
    This is main screen. User have to choice what he wants.
    """
    choice = input(
        """
 0️⃣   Exit
 1️⃣   See The Menu
 2️⃣   Add a New Item
 3️⃣   Change The Price of an Item
 4️⃣   Delete an Item
 5️⃣   Save The Menu External Place
"""
    )
    if choice == "0":
        user_wants_continue = False
    elif choice == "1":
        print(printMenu(menuDic))
    elif choice == "2":
        createMenu()
    elif choice == "3":
        changetheprice()
    elif choice == "4":
        deleteAnItem()
    elif choice == "5":
        saveMenu()
    else:
        print(
            "Gecerli bir giris yapmadiniz.\n 0-1-2-3-4-5 rakamlarindan birine basmalisiniz."
        )
