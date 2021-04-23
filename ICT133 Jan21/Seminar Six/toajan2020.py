def Q2c():

    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest

    def secondLargest(aList):
        
        y = aList.copy()
        theLargest = largest(y)
        y.remove(theLargest)
        
        return(largest(y))

    aList = [2, 5, 1, 6]
    print(secondLargest(aList))
    print(largest(aList))

Q2c()

def Q2b():

    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest


    students = {'John':53, 'Ann':62, 'Peter':45, 'Tom':62}
    theHighestMark = largest(list(students.values()))
    print(f"The highest mark is {theHighestMark}")

    #names = [k for k, v in students.items() if v == theHighestMark ]

    names = []
    for k, v in students.items():
        if v == theHighestMark:
            names.append(k)

    print("The Top Scorers")
    for i in names:
        print(f"{i}")

    print(f"The number of students socring {theHighestMark} is {len(names)}")
        
#Q2b()

def Q2a():

    def larger(a, b):
        return a if a > b else b

    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest

    def largest2(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if larger(theLargest, aList[i]) != theLargest:
                theLargest = aList[i]
        return theLargest


    aList = [2, 7, 4, 3]
    print(largest(aList))
    print(largest2(aList))

#Q2a()

def Q1b():

    s = 'abcdefgh'
    newS = ''
    for i in range(0, len(s), 3):
        newS += s[i].upper() + s[i+1:i+3]
        print(newS)

#Q1b()

def Q1a():

    a, b = 16, 5
    c = 0

    while True:
        if a >= b:
            c = c + 1 #c += 1
            a = a - b
        else:
            break
    
    print(a, b, c)

#Q1a()
