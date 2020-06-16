import functions

'''
Define a function called "count" that has two parameters, called "FirstSequence" and "item"
return the number of times the item occurs in the FirstSequence.
for example: count ([1,2,1,1]), 1) should return 3 (because 1 appears 3 times in the list). 
'''
'''
print(functions.count([1,3,4,4], [2,5,5,4,4,4,4],4))
'''
'''
Recursive functions
'''
'''

def recursive (x):
    x+=1
    recursive(x)


recursive(0)
'''
'''

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))

num = 998
print("The factorial of", num, "is", factorial(num))
'''

'''create a recursive function , that depending on the value given to it, will print "hello world" a number of times
'''
'''
def helloWorld (x):
    if x == 0:
        print("Hello world")
    else:
        print("Hello world")
        helloWorld(x-1)

helloWorld(3)
'''

''' Write lambda that adds 15 to a given number'''
'''
lambdaVariable = lambda x: x+15
print(lambdaVariable(3))
'''

'''
Ask a user for an input. if that input is not a number , let them know it is not a number. and if
it is a number,say ok good.
'''

'''

try:
    userInput = int(input("Please write one sign: "))
except:
    print("This is not a number")
else:
    print("It is a number")
'''


'''Ask a user to input a  number, every time they give you an input, you add that input to a list, 10 times.
At any point the user inputs NOT a number, throw an error and go back to asking for inputs.
'''

userInputList=[]
amountOfTimes = 10
while len(userInputList)<10:
    try:
        userInput2= int(input("Please input a number: "))
        userInputList.append(userInput2)
      
    except:
        print("Error")  

print(userInputList)



    

