import random

def slide19():

    def getPlayers():

        players = {}

        while True:
            name = input( 'Enter name: ').capitalize()
            if name == '': break
            players[name] = { 'won': 0, 'guess': 0}
        
        return players

    def rollDice():
        return random.randint(1, 6)

    def getPlayerGuess(name, tries):
        return int(input(f"Try {tries}. {name}, enter guess: "))

    def checkGuess(players, diceValue):

        correct = False

        for k, v in players.items():
            if diceValue == v['guess']:
                print(f"{k}, you got it!")
                v['won'] += 1
                correct = True
            else: 
                print(f"{k},incorrect")
        
        return correct

    def playGuessingGame(players, diceValue):

        for tries in range(1,4):
            
            for k, v in players.items():
                v['guess'] = getPlayerGuess(k, tries)
                
            if checkGuess(players, diceValue):
                break

        else:
            print(f"Sorry, value is {diceValue}")

    def byScore(elem):
        return(elem[1]['won'])
    
    def sortBasedOnScore(players):
        
        scoreList = list(players.items())
        scoreList.sort(key = byScore, reverse = True)   
        return scoreList

    def printScoreSummary(players):

        # for k, v in players.items():
        #     print(f"{k} won {v['won']} game{'' if v['won'] < 2 else 's'}")

        sortedScores = sortBasedOnScore(players)

        for item in sortedScores:
            print(f"{item[0]} won {item[1]['won']} game{'' if item[1]['won'] < 2 else 's'}")

    def main():

        players = getPlayers()
        playAgain = 'y'
        
        while playAgain[0].lower() in 'yY':
            diceValue = rollDice()
            playGuessingGame(players, diceValue)
            printScoreSummary(players)
            playAgain = input( "Continue? y/n: ")
        
        print( "End game")
    
    main()

slide19()