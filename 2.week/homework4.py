hangmanList = ["apple", "banana", "strawberry", "blueberry", "pear", "kiwi", "grape", "orange", "lemon", "mango"]

import random 
word=random.choice(hangmanList)
print(word)

wordToGuessList=[]
for x in word:
    wordToGuessList.append(x)

wordToGuessList2=wordToGuessList.copy()

emptyList=[]
for x in wordToGuessList2:
    emptyList.append("_")

print(emptyList)
lives=10

playerGuess = input("Please guess a letter: ")
while lives!=0:
    if playerGuess==word:
        print("Well done")
        break
    if playerGuess in wordToGuessList2:
        for x in wordToGuessList2:
            if x==playerGuess:
                indexOfLetter=wordToGuessList2.index(x)
                emptyList[indexOfLetter]=x
                wordToGuessList2[indexOfLetter]=0
        print(emptyList)
        if emptyList==wordToGuessList:
            print("All guessed")
            break
        playerGuess=input("Please try one more: ")
    else:
        lives=lives-1
        if lives==0:
            print("Game over")
            break    
        playerGuess=input("Please try again: ")



    




'''
    playerGuess=input("Please try one more: ")
    lives=lives-1
    while playerGuess in wordToGuessList:
        for x in wordToGuessList:
            if x==playerGuess:
                indexOfLetter=wordToGuessList.index(x)
                emptyList.insert(indexOfLetter, x)
                emptyList.pop(indexOfLetter+1)
                wordToGuessList.insert(indexOfLetter, 0)
                wordToGuessList.pop(indexOfLetter+1)
                print(emptyList)
                playerGuess=input("Please try one more: ")
                lives=lives-1
                if x!=playerGuess:
                    playerGuess = input("Please try again: ")
                    lives=lives-1
                    '''


                    
