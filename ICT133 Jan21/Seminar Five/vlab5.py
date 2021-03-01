def Q5():

    #Q4a

    def menuGetOption():
        return int(input('''
    Menu
1. Add Marks
2. Adjust Marks
3. Remove Student
4. Display Student Marks
0. Quit
Enter option: '''))

    def addMarks(marks):
    
        name = input(f"Enter Name : ")

        if marks.get(name):
            print(f"Student already exists!")
        else: 
            work = float(input(f"Enter course work: "))
            exam = float(input(f"Enter exam: "))
            marks[name] = [work, exam]
            print(f"Added")

    def adjustMarks(marks):

        name = input(f"Enter student: ")
        
        if marks.get(name) == None:
        
            print(f"Name not found!")
        
        else:
        
            aMark = marks.get(name)
            print(f"({name} found. marks displayed)")
            print(f"Course Work: {aMark[0]}")
            print(f"Exam: {aMark[1]}")
        
            part = input(f"Update C or E: ")
        
            if part == 'C':
                c = float(input(f"Enter Course Work "))
                aMark[0] = c
                print(f"Course Work adjusted to {c}")
            else:
                e = float(input(f"Enter Exam "))
                aMark[1] = e
                print(f"Exam adjusted to {e}")

    def removeStudent(marks):

        name = input(f"Enter student name: ")
        
        if marks.get(name) == None:
            print(f"Student not found!")
        else:
            marks.pop(name)
            print(f"{name} is removed")
    
    def displayMarks(marks):
      
        print(f"Name  Cw   Ex   Overall Grade")     
        for key, item in marks.items():         
            print(f"{key:<6s}{item[0]:<5.1f}{item[1]:<5.1f}{(item[0]+item[1])/2:<8.1f}{'P' if (item[0]+item[1])/2 >= 50 else 'F'}")

    marks = { 'John':[0,0], 'Jane':[0,0], 'Peter':[0,0], 'Joe':[0,0] }

    option = menuGetOption()
    print(f"The option chosen is {option}")

    while option != 0:
        
        if option == 1:
            addMarks(marks)
            #print(currs)
        elif option == 2:
            adjustMarks(marks)     
            #print(currs)
        elif option == 3:
            removeStudent(marks)
        elif option == 4:
            displayMarks(marks)
        
        option = menuGetOption()
        print(f"The option chosen is {option}")

Q5()

def Q4():

    currs = {'USD': 0.73, 'RMB':5.01, 'HKD':5.73 }

    #Q4a
    def menuGetOption():
        return int(input('''
    Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
Enter option: '''))

    def addCurrency(currs):
    
        country = input(f"Enter currency: ")

        if currs.get(country):
            print(f"Currency already exists!")
        else: 
            rate = float(input(f"Enter rate: "))
            currs[country] = rate

    def adjustCurrency(currs):

        country = input(f"Enter currency: ")
        
        if currs.get(country) == None:
            print(f"Currency not found!")
        else:
            rate = currs.get(country)
            print(f"Rate is {rate}")
            rate = float(input(f"Enter new rate: "))
            currs[country] = rate
            print(f"{country} adjusted to {rate}")

    def removeCurrency(currs):

        country = input(f"Enter currency: ")
        
        if currs.get(country) == None:
            print(f"Currency not found!")
        else:
            currs.pop(country)
            print(f"{country} is removed")
    
    def displayCurrency(currs):
        print(f"Currency    Rate")     
        for key, item in currs.items():         
            print(f"{key:<12s}{item:<7.2f}")

    option = menuGetOption()
    print(f"The option chosen is {option}")

    while option != 0:
        
        if option == 1:
            addCurrency(currs)
            #print(currs)
        elif option == 2:
            adjustCurrency(currs)     
            #print(currs)
        elif option == 3:
            removeCurrency(currs)
        elif option == 4:
            displayCurrency(currs)
        
        option = menuGetOption()
        print(f"The option chosen is {option}")
#Q4()

def Q3():

    tutGp = {'T01': 28, 'T02':15, 'T03':28, 'T04':25, 'T05':29, 'T06':22 }

    def printSummary(tutGp): # Q3a 

        print(f"TG Size")

        size = 0
        for item in tutGp.items():
            print(f"{item[0]:<4s}{item[1]:<4d}")
            size += int(item[1])
        print(f"Total number of students {size}")   

    def updateTutGp(tutGp): # Q3b

        gp = input("Enter tutoral group: ")
        if gp in tutGp.keys():
            print(f"Tutorial group exists. Class size is {tutGp[gp]}")
            delta = int(input("Enter size to add/subtract group: "))
            tutGp[gp]+=delta
        else:
            delta = int(input("Enter class size: "))
            tutGp[gp]=delta
    
    def increaseByThree(tutGrp):

        for k, v in tutGrp.items():
            v = int(v)
            if v + 3 > 30:
                print(f"{k} adjusted to max 30")
            else:
                print(f"{k} adjusted to {v+3}")

    printSummary(tutGp)
    updateTutGp(tutGp)
    increaseByThree(tutGp)
    print(tutGp)

#Q3()

def Q2b():

    def getPlayerNames():
        
        players=[ ]

        for i in range(2):
            player = input(f"Player {i+1} name is ")
            players.append(player)

        return [ players ]

    def inputGameScores(scoreList):

        count = 1
        while True:
            scores=input(f"Game {count} score {scoreList[0][0]} vs {scoreList[0][1]}: ")
            if scores == "": break
            score1, score2 = scores.split('-')
            scoreList.append([score1, score2])

    def displayGameScore(gameScore):

        playerA = gameScore[0][0]
        playerB = gameScore[0][1]
        print(f"Player {playerA} vs {playerB} ")

        a = 0
        b = 0

        for index, item in enumerate(gameScore[1:]):
            print(f"Game {index+1} {item[0]}-{item[1]}")
            if item[0] > item[1]:
                a+=1
            else:
                b+=1
        
        print(f"Overall {a}-{b}")

        if a > b :
            print(f"Winner is player {playerA}")
        else:
            print(f"Winner is player {playerB}")
    

    scoreList = getPlayerNames()
    print(f"{scoreList}")
    inputGameScores(scoreList)
    displayGameScore(scoreList)

#Q2b()

def Q2a():

    gameScore1=[['A','B'],[21,11],[19,21],[20,21]]
    gameScore2=[['A','B'],[21,1],[21,10]]

    def displayGameScore(gameScore):

        playerA = gameScore[0][0]
        playerB = gameScore[0][1]
        print(f"Player {playerA} vs {playerB}")

        a = 0
        b = 0

        for index, item in enumerate(gameScore[1:]):
            print(f"Game {index+1} {item[0]}-{item[1]}")
            if item[0] > item[1]:
                a+=1
            else:
                b+=1
        
        print(f"Overall {a}-{b}")

        if a > b :
            print(f"Winner is player {playerA}")
        else:
            print(f"Winner is player {playerB}")
    
    displayGameScore(gameScore1)
    displayGameScore(gameScore2)

#Q2a()

def Q1c():

    scores_in = [ [7.9,8.0,9.0,9.0,8.5,9.7],[7.8,8.5,9.1,9.2,8.8,9.8],[8.2,8.4,9.5,9.2,9.0,9.7] ]
    scores_out = [ [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

    def Q1a(scores):

        # Q1.a

        a1 = "A1"
        a2 = "A2"
        a3 = "A3"
        total = "Total"

        print(f"Diver {a1:<4s}{a2:<4s}{a3:<4s}{total:<5s}")

        for index, aList in enumerate(scores):
            print(f"{index+1:^6d}", end="")
            sum = 0.0

            for i in range(len(aList)):
                print(f"{aList[i]:<4.1f}", end="")
                sum += aList[i]
            
            print(f"{sum:<5.1f}")

    for i in range(len(scores_in)):
        for j in range(len(scores_in[i])):
            scores_out[j][i] = scores_in[i][j]
    
    Q1a(scores_out)

#Q1c()

def Q1b():

    scores=[[7.9,7.8,8.2],[8.0,8.5,8.4],[9.0,9.1,9.5],[9.0,9.2,9.2],[8.5,8.8,9.0],[9.7,9.8,9.7]]

    # Q1.a

    total = "Total"
    print(f"Diver {total:<5s}")

    def keyFunc(elem):
        return elem[1]

    def totalScores(scores):

        aTotalList=[]

        for index, aList in enumerate(scores):
            sum=0.0
            for i in range(len(aList)):
                sum += aList[i]
            
            aTotalList.append([index+1, sum])

        return aTotalList

    aTotalList = totalScores(scores)

    aTotalList.sort(key=keyFunc, reverse=True)

    for item in aTotalList[:3]:
        print(f"{item[0]:^6d}{item[1]:<4.1f}")
    
    #print(aTotalList)

#Q1b()

def Q1a():

    scores=[[7.9,7.8,8.2],[8.0,8.5,8.4],[9.0,9.1,9.5],[9.0,9.2,9.2],[8.5,8.8,9.0],[9.7,9.8,9.7]]

    # Q1.a

    a1 = "A1"
    a2 = "A2"
    a3 = "A3"
    total = "Total"

    print(f"Diver {a1:<4s}{a2:<4s}{a3:<4s}{total:<5s}")

    for index, aList in enumerate(scores):
        print(f"{index+1:^6d}", end="")
        sum = 0.0

        for i in range(len(aList)):
            print(f"{aList[i]:<4.1f}", end="")
            sum += aList[i]
        
        print(f"{sum:<5.1f}")
        
#Q1a()