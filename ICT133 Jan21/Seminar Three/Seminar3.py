def slide4():

    x = 11

    if x <= 15: 
        print( x, end = " " )
        x = x + 1

#slide4()

def slide5():

    for i in range(5):
        print(i, end=" ")
    print("")
    
    for i in range(0, 5, 1):
        print(i, end=" ")
    print("")
    
    for i in "012345"[0:5:1]:
        print(i, end=" ")
    print("")

#slide5()

def slide6():

    for x in range(1, 16):
        print( x, end = " " )
    print("")
    
    for x in range(1, 16, 1):
        print( x, end = " " )
    print("")

    for x in range(1, 16, 2):
        print( x, end = " " )
    print("")

    for x in range(10, 0, 1):
        print( x, end = " " )
    print("")

#slide6()

def slide8():

    n = int(input("How many numbers do you have? "))

    if n <= 0:
        print(f"\nThe number {n} is invalid")
    else:
        sum = 0.0

    for i in range(n):
        x = float(input("Enter a number >> "))
        sum = sum + x
    
    print(f"\nThe average of the numbers is {sum/n:.2f}") 

#slide8()

def slide9():

    sum, n, m = 0, 5, 6 # multiply 5 x 6

    for i in range(n):
        sum += m

    print(f"{n} * {m} = {sum}")

#slide9()

def slide10():

    for ch in "Spam!":
        print (ch, end=" ")

#slide10()

def slide13():

    x = 11 

    while x <= 15:
        print(x, end = " ")
        x = x + 1
    print("")
    
    for x in range(11,16):
        print(x, end = " ")
    print("")

#slide13()

def slide16():

    i = 0
    while True:
        if i > 10: break
        print(i)
        i += 1
    
#slide16()

def slide17():

    sum, count = 0.0, 0
    
    moredata = "yes"

    while moredata[0] == "y":
        x = float(input("Enter a number >> "))
        sum += x
        count += 1
        moredata = input("Do you have more numbers (yes or no)? ")
    
    print(f"\nThe average of the numbers is {sum/count}")

#slide17()

from random import randrange

def slide23():
    
    tries = 1

    diceValue=randrange(1,10)

    maxNumberOfTries = 4

    while tries <= maxNumberOfTries:
        guess = int(input(f"Try {tries}. Enter guess: "))
        if diceValue == guess:
            print("You got it!")
            break
        print("Incorrect")
        tries += 1
        if tries > maxNumberOfTries:
            print(f"Sorry, value is {diceValue}")

#slide23()

def slide24():
    
    tries = 1

    diceValue=randrange(1,10)

    maxNumberOfTries = 4

    while tries <= maxNumberOfTries:
        guess = int(input(f"Try {tries}. Enter guess: "))
        if diceValue == guess:
            print("You got it!")
            break
        print("Incorrect")
        tries += 1
    else:
        print(f"Sorry, value is {diceValue}")

#slide24()

def slide28():

    playAgain = "yes"

    while playAgain[0].lower() == 'y':

        tries = 1

        diceValue=randrange(1,10)

        maxNumberOfTries = 3

        while tries <= maxNumberOfTries:
            guess = int(input(f"Try {tries}. Enter guess: "))
            if diceValue == guess:
                print("You got it!")
                break
            print("Incorrect")
            tries += 1
        else:
            print(f"Sorry, value is {diceValue}")
        
        playAgain = input("Continue? (Y/N)")

    print(f"End of the Game")

#slide28()

def slide34():

    def happy():
        print("Happy Birthday to You")

    def sing(person):
        happy()
        happy()
        print(f"Happy birthday, dear {person}")
        happy()

    sing("Peter")

    return "That is the end of the Song"

#print(slide34())

def listExample():

    #list comprehension slide 21 of Seminar 4

    aList = [k for k in "abc"]

    for i in aList:
        print(i, end=" ")
    print("")

#listExample()

def menu():
    return int(input(''' 
Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit 
Enter Choice '''))

def lab3_q5():

    choice = 6

    while choice != 0:
        choice=menu()
        print(f"Option {choice} is selected")

    print("End of Choice")

#lab3_q5()

def sem4_slide15():

    fileName = input("What file are the numbers in? ")
    fileName2 = input("What output file to store the resutls? ")

    infile = open(fileName,'r')
    outfile = open(fileName2, 'w')

    sum, count = 0.0, 0
    for line in infile: # lines separated by \n
        num1, num2 = line.split()
        num1 = float(num1)
        num2 = float(num2)
        sum += (num2 + num2)
        count = count + 2

    #print(f"\nThe average of the numbers is {sum/count:0.3f}", file=outfile)
    outfile.write(f"\nThe average of the numbers is {sum/count:0.3f}")

    infile.close()
    outfile.close()

#sem4_slide15()

def sem5_slide11():

    aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    aDict = {'January': 31, 'February': 29, 'March': 31, \
    'April': 30, 'May': 31, 'June': 30, \
    'July': 31, 'August': 31, 'September': 30,\
    'October': 31, 'November': 30, 'December': 31}

    for k, v in aDict.items():
        print(f"Month {k} has {v} days")

sem5_slide11()

def sem5_slide12():

    passwdDict = {}

    for line in open('passwords.txt', 'r'):
        user, passwd = line.split()
        passwdDict[user] = passwd

    # slide 14
    # { k : v }
    for k, v in passwdDict.items():
        print(f"{k} {v}")

    print("End Of Slide12()")

#sem5_slide12()