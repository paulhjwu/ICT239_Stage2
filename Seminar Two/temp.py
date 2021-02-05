import math
from math import sqrt

def main():

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discrim = b * b - 4 * a * c

    if discrim < 0:
        print("No real roots")
    #if discrim >= 0:
    else:
        discRoot = sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print(root1, root2)

main()