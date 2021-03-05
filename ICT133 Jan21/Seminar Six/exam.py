def Q3():

    soups = {"Clam Chowder": 50, "Mushroom": 50, "Tomato": 50, "Pumpkin": 50, "Oxtail": 50}

    def displayMenu():
        return int(input('''1. Purchase Soup
2. Replenish Soup
3. Print Stock
0. Exit 
Enter your choice '''))

    def keyFunc(elem):
        return elem[0]

    def printStock(soups):

        menu = []

        for item in soups.items():
            menu.append(list(item))
        
        menu.sort(key=keyFunc)

        for elem in menu:
            if elem[1] >= 0:
                print(f"Soup {elem[0]} has {elem[1]} servings left")
        
    def purchaseSoup(soups):

        printStock(soups)  
        soupToPurchase = input("Which soup to be purchased ")

        if soupToPurchase in soups:

            quantity = int(input(f"How many portions would be purchased? "))

            possibleQuanity = quantity if quantity <= soups[soupToPurchase] else soups[soupToPurchase]

            if quantity > possibleQuanity :
                print(f"Only {possibleQuanity} out of {quantity} {soupToPurchase} can be purchased")
                print(f"{quantity - possibleQuanity } of {soupToPurchase} cannot be purchased")
                soups[soupToPurchase] = 0
            else:
                print(f"{quantity} of {soupToPurchase} are purchased")
                soups[soupToPurchase] -= quantity
        
        else:
            print(f"Soup not found!!")

        return soups
    
    def replenishSoup(soups):

        printStock(soups)

        soupToReplenish = input(f"Which soup to be replenished? ")
        if soupToReplenish in soups:
            quantity = int(input(f"How many portions would be replenished? "))
            soups[soupToReplenish] += quantity
        else:
            print(f"Soun not found in the Stock")


    #displayMenu()
    #purchaseSoup(soups)
    #print(soups)
    #replenishSoup(soups)
    #print(soups)

    choice = displayMenu()

    while True:
    
        if choice == 0: break

        if choice == 1:
            purchaseSoup(soups)
        elif choice == 2:
            replenishSoup(soups)
        elif choice == 3:
            printStock(soups)

        choice = displayMenu()

Q3()


# Quesiton 1.b
def f(s):

    n = 0 

    x = 0

    while x < len(s):

        if int(s[x]) % 2 == 0: 
            n += 1
        x += 1

    return n

# def f(s):

#     n = 0 

#     for c in range(len(s)): 
#         if int(s[c]) % 2 == 0: 
#             n += 1

#     return n

#print(f('162534'))

#Qustion 1a i and ii

def subtract(x, y):

    z = 0

    if x < y :
        buffer = x
        x = y
        y = buffer
        swopped = True

    while x > y:
        x -= 1
        z += 1

    if not swopped:
        print(z)
    else:
        print(-z)

#subtract(2, 3)