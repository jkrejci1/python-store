#Jack Krejci
#The Jungle Store

#Welcome to the jungle title
print("-" * 70)
print("%s" % "WELCOME TO THE JUNGLE".center(70))
print("%s" % "We've Got Fun and Games".center(70))
print("-" * 70)
print()

#Functions

#Main Menu Function
def show_menu_and_get_choice():
    print()
    print("Choices")
    print("1. Shop")
    print("2. See cart")
    print("3. Remove items")
    print("4. Pay and Exit")
    try:
        choice = int(input("Enter number of choice: "))
        print()
        return choice
    except:
        print("That's not a choice!")
        print()


#Main Code
fname = "jungle_items.txt"
fvar = open(fname,"r")
choice = show_menu_and_get_choice()

#Lists to be used for storing items initially
item = []
cost = []

#Lists for user action
cart = []

#Takes in the file an creates our new lists
for line in fvar:
    line = line.strip() #Gets rid of end-of-line marker
    if line != "": #To not process empty lines where all that whitespace is at the end below the last name
        parts = line.split("\t") #\t is code for the tab key
        item.append(parts[1:3])

#Loop to bring user to a decision when they haven't chosen to pay and exit
while choice != 4:
    #If the user wants to add an item to their cart
    if choice == 1:
        print("What would you like to purchase?")
        print()
        for i,items in enumerate(item): #items is used so you dont permanately change the item list
            print("%2d. %s ($%s)" % ((i+1),items[0],items[1]))
        print()
    #Create a loop in order to correct the user if they keep entering a number not in the list
        loop = True
        while loop == True:
            try:
                selection = int(input("Enter number of choice: "))
                #Translates user selection to the actual index values of the list
                selection -= 1
                cart.append(item[selection])
                break
            except:
                print("That isn't in the list!")
                
        #Show menu to the user again to make a choice remember "cart" now contains a list of items that were chosen in this function        
        
    #If the user wants to see their cart
    elif choice == 2:
        #Tell user if their cart is empty
        if cart == []:
            print("Your cart is empty.")
        else:
            #List out all the items in the cart
            print("Here are the items in your cart:")
            for chosen in cart: #items is used so you dont permanately change the item list
                print("%-19s $%6s" % ((chosen[0]),(chosen[1])))
            print()
            
    #If the user wants to remove items from their cart         
    elif choice == 3:
        #Notify the user if their cart is empty
        if cart == []:
            print("Your cart is empty. Can't remove any items.")
        #For when the list isn't empty preform this code
        else:
            #List out all the items that the user currently has 1 by 1
            print("Here are the items in your cart:")
            for i,display in enumerate(cart):
                print("%2d. %s" % ((i+1),display[0]))
            #Create loop in order to have the user enter a valid number in the list
            remove_loop = True
            while remove_loop == True:
                try:
                    #Have the user enter the number of the item they want to remove
                    remove_select = input("Enter the item to remove, or 'a' to clear all items: ").lower().strip()
                    if remove_select == "a":
                        cart.clear()
                        break
                    
                    if remove_select != "a":
                        #Translates user selection to the actual index values of the list
                        remove_select = int(remove_select) #Converts the number which was originally a string to an integer
                        remove_select -= 1
                        cart.pop(remove_select)
                        break
                except:
                    print("That isn't a valid number or a!")
     #Give the user the option to select what else they'd like to do
    choice = show_menu_and_get_choice()

#Runs this code when the choice IS 4
while choice == 4:
    #Accounts for if the cart is empty
    if cart == []:
        print("Your cart is empty. You owe us nothing.")
        print()
        break
    else:
    #Code runs when cart isn't empty
        total_cost = 0
        print("Here is what you purchased:")
        #Displays all the items in your cart
        for i,display in enumerate(cart):
                print("%2d. %-15s $%6s" % ((i+1),display[0],display[1]))
                cost.append(float(display[1]))
        print()
        #Adds up the total cost 
        for costs in cost:
            total_cost += costs
        #Displays the total cost of all items in cart
            
        print("%-19s $%6.2f" % ("Total cost:",total_cost))       
        break      
        
        print()

#Close the file being used      
fvar.close()

#Say goodbye
print("Thank you for shopping at the jungle!")

