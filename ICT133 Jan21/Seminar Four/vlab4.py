def slide16_S5():

    def getScores():
        return {'Evelyn': 21, 'Helen': 33, 'George': 35, 'Alice': 22}
    
    def byScore(elem):
        return(elem[1])

    def sortBasedOnScore(scores):
        scoreList = list(scores.items())

        scoreList.sort(key = byScore, reverse = True)
        
        return scoreList

    def main():

        scores = getScores()

        sortedScores = sortBasedOnScore(scores)

        for item in sortedScores:
            print(f"{item[0]} got {item[1]} marks")

    main()

slide16_S5()

def slide15_S5():

    def getScores():
        return {'Evelyn': 22, 'Helen': 33, 'George': 33, 'Alice': 22}
    
    def searchScore(scores, name):
        return scores.get(name, 'Not recorded')

    def main():
        scores = getScores()
        while True:
            
            name = input("Enter name of student or <ENTER> to end: ").capitalize()
            
            if name == '': break
            print(searchScore(scores, name))
    main()

#slide15_S5()

def slide5_S5():

    def getScores():
        return [['Evelyn', 22], ['Helen', 33], ['George', 33], ['Alice', 22]]
    
    def searchScore(scores, name):
        score = [elem[1] for elem in scores if elem[0] == name]
        if score != []:
            return score[0]
        else:
            return 'Not recorded'

    def main():

        #scores = [['Evelyn', 22], ['Helen', 33], ['George', 33], ['Alice', 22]]
        scores = getScores()
        
        while True:
            
            name = input("Enter name of student or <ENTER> to end: ").capitalize()
            if name == '': break
        
            print(searchScore(scores, name))

    main()

#slide5_S5()

def q4():

    weight = (2, 7, 6, 5, 4, 3, 2)
    conversionTable = [i for i in "ABCDEFGHIZJ"]
    theNRIC=input("Enter NRIC ")

    sum = 0
    for i in range(len(theNRIC)-2):
        sum += (int(theNRIC[i+1])*weight[i])

    remainder = sum % 11

    checkNum = 11 - remainder

    if theNRIC[len(theNRIC)-1] != conversionTable[checkNum-1]:
        print(f"The reference character is not correct")
    else:
        print(f"The reference character is correct")

#q4()

from random import choice

def q3():

    diceCount = [0, 0, 0, 0, 0, 0, 0]

    for i in range(100):
        diceValue = choice([1, 2, 3, 4, 5, 6])
        #diceCount[diceValue] =  diceCount[diceValue]+1
        diceCount[diceValue] += 1
    
    print(f"Dice      Occruence")
    for i in range(6):
        print(f"{i+1:<10d}{diceCount[i+1]}")

#q3()
