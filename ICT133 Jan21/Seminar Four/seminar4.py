def slide34():

    def getPlayerGuess(tries):
        return int(input(f"Try {tries}. Enter guess: "))

    def checkGuess(guess, diceValue):

        success = (diceValue == guess)

        if success:
            print("You got it!")
        else:
            print("Incorrect")

        return success

    def playGuessingGame(diceValue):

        for tries in range(1, 4):
            guess = getPlayerGuess(tries)
            if checkGuess(guess, diceValue):
                break
        
        if tries >= 3:
            print(f"Sorry, you have tried {tries} times, the value is {diceValue}")

    from random import randint

    def rollDice():
        return randint(1, 6)

    def main():

        playAgain = 'y'

        while playAgain[0].lower() in 'yY':
            diceValue = rollDice()
            playGuessingGame(diceValue)
            playAgain = input("Continue? y/n: ")
        print("End game")
    
    main()

slide34()

def slide28():

    def double(x):
        x = x.append(2)
        z = x
        return z

    def main():
        x = [10]
        y = double(x)
        print(x, y)

    main()

#slide28()

def slide26():
    
    def double(value):
        value = 2 * value
        z = value
        return z

    def main():
        x = 10
        y = double(x)
        print(x, y)
    #   print(value)

    main()

#slide26()

def slide22():

    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', \
    'July', 'August', 'September', 'October', 'November', 'December']
    
    maxMonths=[monthName[index] for index in range(12) if (month[index] == max(month))]
    print(maxMonths)

    # maxDays = max(month)
    
    # for index in range(12):
    #     if month[index] == maxDays:
    #         print(monthName[index])

#slide22()

def slide20():

    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', \
    'July', 'August', 'September', 'October', 'November', 'December']
    
    maxDays = max(month)
    
    for index in range(12):
        if month[index] == maxDays:
            print(monthName[index])

#slide20()


def slide19():

    x = 29
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if x in month:
        print('Leap year')
    else:
        print('Not a leap year')

#slide19()

def tmaQ1cii():
    
    aisleVisitList = []

    theAisleToVisit = int(input("Enter the aisle number to visit: "))

    while True:
        if theAisleToVisit != 0:
            aisleVisitList.append(theAisleToVisit)
            theAisleToVisit = int(input("Enter the aisle number to visit: "))
        else:
            break
    
    print(aisleVisitList)

#tmaQ1cii()

def slide16():

    myList = [34, 26, 15, 10]
    myList[2] = 12
    print(myList)

    myTuple = (34, 26, 15, 10)
    #myTuple[2] = 12
    aElem = myTuple[2]
    print(myTuple)

#slide16()

def slide13():

    for i in "abcde":
        print(i)

    for i in [1, 2, 3, 4, 5]:
        print(i)

    for i in (6, 7, 8, 9, 10):
        print(i)

#slide13()

def slide7():

    fileName = input("What file are the numbers in? ")  
    infile = open(fileName,'r')

    sum, count = 0.0, 0

    for line in infile:
        for xStr in line.split(","):
            sum = sum + float(xStr)
            count = count + 1

    print("\nThe average of the numbers is", sum/count)
    infile.close()

#slide7()

def slide6():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    outfile = open(fileName + "1.out", 'w')
    sum, count = 0.0, 0

    for line in infile: # lines separated by \n
        sum = sum + float(line)
        count = count + 1

    print("\nThe average of the numbers is", sum/count)
    #print( "\nThe average of the numbers is", sum/count, file =outfile)
    outfile.write(f"\nThe average of the numbers is, {sum/count}")
    infile.close()
    outfile.close()

#slide6()

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    sum, count = 0.0, 0

    for line in infile: # lines separated by \n
        sum = sum + float(line)
        count = count + 1

    print("\nThe average of the numbers is", sum/count)
    infile.close()

#main()

def byScore(item):
    return item[0]

def trial():

    aList = [(1, 2), (2, 1)]
    
    sorted(aList)

    aList.sort(key=byScore, reverse=True)
    
    print(aList)

#trial()