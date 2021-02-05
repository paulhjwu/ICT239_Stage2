import math
from math import ceil

def q7():

    nric = input("Enter NRIC ")

    if len(nric) != 9:
        print(f"Length must be exactly 9 characters")
    elif nric[0].upper() not in "STFG":
        print(f"The first letter must be S, T, F, or G ")
    elif not nric[1:8].isdigit():
        print(f"Must consist of 7 digits")
    elif not nric[-1].isalpha():
        print(f"The reference letter must be an alphabet")
    else:
        print("Nric is valid")

#q7()    

def q5():

    dataUsed = float(input("Amount of data used (GB) "))

    charge = 5

    if dataUsed > 2:
        surplus = dataUsed - 2
        charge += ceil(surplus * 10)
    
    print(f"Charge is $ {charge:6.2f}")

#q5()

def q4():

    theString = input("Enter the string ")

    theReverse = theString[-1::-1]

    if theString == theReverse:
        print(f"The string {theString} is a palindrome")
    else:
        print(f"The string {theString} is not a palindrome")

#q4()


def q3():

    firstN, secondN = input("Enter two numbers: ").split()

    firstN = int(firstN)
    secondN = int(secondN)

    if firstN == secondN:
        print(f"The two numbers are equal")
    else:
        print(f"The two numbers are not equal")

#q3()


def q2():

    firstP, secondP = input('Enter strings: ').split()

    firstP = firstP[-1::-1]
    secondP = secondP[-1::-1]

    print(f"Output: {firstP} {secondP}")

#q2()

def q1():

    # "joe@suss.edu.sg"  [start:end:incre]

    email = input('Enter email: ')
    index = email.find('@')

    if index == -1:
        print("Invalid email")
    else:
        name = email[:index]
        org = email[index+1:]
        print(f'Name is {name}')
        print(f'Organization is {org}')

#q1()