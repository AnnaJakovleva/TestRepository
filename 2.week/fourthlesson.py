'''
listValues = [1,2,3,4,5,6,7,8,9,10]
listValues2 = [6,2,3,9,5,6,28,8,22,10]

nestedList= []
nestedList.append(listValues)
nestedList.append(listValues2)

print(nestedList)
print(nestedList[0][0])
print(nestedList[1][0])


for x in nestedList:
    for z in x:
        print(z)


gameIsPlaying = True

while gameIsPlaying:
    print("The game is being played")

points = 0

while points<10:
    print("The game is being played")
    if points == 5: pass
    points +=1
else:
    print("The loop has ended")    

'''  

import random 
import datetime
import math
'''
randomNumber = random.randint(0,10)
print(randomNumber)

randomPopulation = random.sample(range(10000000), 60)
print(randomPopulation)
'''
'''
current = datetime.time()
print(current)
'''
'''
x=datetime.datetime.now()

print(x.strftime("%a"))
print(x.strftime("%H"))
print(x.strftime("%p"))
print(x.strftime("%Z"))
print(x.strftime("%j"))
'''
'''
import time

time.sleep(10)
'''

''' Write a program to guess a number between 1 to 9. User is prompted to guess the number, if they guess
incorrectly say "wrong number", and ask for input again. If they do guess it, say "Well guessed" 
and exit the program.
'''
'''

import random 
randomNumber = random.randint(0,9)
print(randomNumber)
userInputNumber = int(input("Please guess the number "))

if randomNumber != userInputNumber:
    gameIsPlaying1 = True
else:
    gameIsPlaying1 = False
    print("Well guessed")

while gameIsPlaying1:
    if randomNumber != userInputNumber:
        print("Wrong guess")
        userInputNumber=int(input("Guess again "))
    if randomNumber == userInputNumber:
        print("Well guessed")
        gameIsPlaying1 = False

'''
''
import random 
randomNumber = random.randint(0,9)
print(randomNumber)
userInputNumber = int(input("Please guess the number "))

if userInputNumber!=randomNumber:
    print("Wrong guess")
    userInputNumber2=int(input("Please try again "))
    while userInputNumber2!=randomNumber:
            print("Wrong guess")
            userInputNumber2=int(input("Please try again "))
            if userInputNumber2==randomNumber:
                print("Well done")
                break
else:
    print("Well done")


    



