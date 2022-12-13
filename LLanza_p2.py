#Lena Lanza
# Returns the price for a given item.
def getItemPrice(categoryDict, item):
    if item in categoryDict.keys():
        return categoryDict[item]
    else:
        return 0

# Returns the totalPrice of the orderList.
def getOrderTotal(menuDict, orderList):
    totalPrice = 0.00
    for menu in menuDict.keys():
        for order in orderList:
            totalPrice += getItemPrice(menuDict[menu], order)
    return totalPrice

# This is given DO NOT change, if this function is not working
# there is an error somewhere else in your code.
def printOrder(orderNumber, orderItems, orderTotal, orderType):
    print("For the following order number: " + str(orderNumber) + ", you ordered a " + orderType + " with the following selections: ", orderItems , " the total for this order will be: $" + str(orderTotal))
    print()

# Print only, Do not use return
def printOrders(finalOrders):
    for key in range(len(finalOrders)):  
        for value in range(len(finalOrders[key])):
         print((finalOrders[key][val]))

# Returns a list holding all of the order options selected.
def makeOrder(menuDict):
    makeOrderList=[]
    for menu in menuDict.keys():
        print("For the category: "+menu+"\nThese are your options:")
        for option in menuDict[menu].keys():
            print(option)
        userCategory = input("What would you want from the "+ menu + " category: ")
        #if userCategory in menuDict:
        makeOrderList.append(userCategory)        
    return makeOrderList

    

def main():
    # DO NOT modify this dictionary
    menuItems = {"Rice": {"White": 7.95, "Brown": 7.95, "No Rice": 7.95},\
    "Beans": {"Black": 0.00, "Pinto": 0.00, "No Beans": 0.00},\
    "Protein" : {"Smoked Brisket": 2.35, "Chicken": 0.00, "Steak": 1.35, "Barbacoa": 1.35, "Carnitas": 0.50, "Sofritas": 0.00, "Veggie": 0.00},\
    "Toppings" : {"Guacamole": 2.50, "Fresh Tomato Salsa": 0.00, "Corn Salsa": 0.00, "Green Chili Salsa": 0.00, "Red Chili Salsa": 0.00, "Sour Cream": 0.00, "Fajitas": 0.00, "Cheese": 0.00, "Lettuce": 0.00, "Queso": 1.45},\
    "Drinks" : {"Fountain Drink": 2.50, "Juice": 3.00, "Bottled Water": 2.60, "No Drink": 0.00},\
    "Sides": {"Chips": 1.70, "Chips w/ Guac": 4.20, "Chips w/ Queso": 4.20, "Chips w/ Salsa": 2.15, "No Side": 0.00}}
    # Create a variable that keeps track of whether the user has entered stop or not
    flag = True
    # Create a variable that keeps track of the order number
    orderNumber = 1
    # Create your outer list that will have the following values:
    # order number, order type (bowl or burrito), a list that holds the current order list, 
    # and the total cost of the order
    finalList = []
    # As long as the user has not entered stop then continue
    while flag:
        # Ask whether the user would like a bowl, burrito, or stop adding orders
        orderType = input("Do you want a bowl or a burrito? ")
        # If the input was stop then come out of the while loop
        if orderType == "stop":
            flag = False
        # If the input was not stop then you should do the following
        else:
            # We will prompt our user to select an order type.
            print("What would you like on your " + orderType + "?")
            # We will call the makerOrder() function to ask the user for a selection for each category.
            currentOrder = makeOrder(menuItems)
            # We will call the getOrderTotal() function to get the total cost for our order. 
            currentOrderTotal = getOrderTotal(menuItems, currentOrder)
            # We will print out our current order 
            printOrder(orderNumber, currentOrder, currentOrderTotal, orderType)
            # We will add our order as the inner list to our outer list
            # The format can be seen below.
            finalList.append([orderNumber, orderType, currentOrder, currentOrderTotal])
            # We increase the order number after we make an order.
            orderNumber += 1

    # Once the user enters "stop" then we print all the orders inside our 2-D list.
    printOrders(finalList)
    
        
main()
