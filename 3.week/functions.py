'''def firstFunction(x,y,z):
    print(x)

firstFunction("test","","")
'''
'''
x=10

def firstFunction(*x):
    print(x)
    x=10

firstFunction("test","second","third")
'''
'''
def firstFunction(x="Hello"):
    print(x)

firstFunction()
'''
'''
def firstFunction(x,z):
    print(x)

firstFunction(z="Test",x="secondtest")
firstFunction("kk","hey")
'''

def firstFunction(x):
    print(x)

def secondFunction(calculationVariable):
    print(calculationVariable+2)

def thirdFunction(x):
    x=x*20
    emptyList=[]
    emptyList.append(x)
    return emptyList

def fourthFunction(list1):
    for x in list1:
        print(x)
    return list1[-1]

def fifthFunction(list2):
    list3=[]
    for x in list2:
        if x not in list3:
            list3.append(x)
    for x in list3:
        if x%2==0 :
            print(x)
    return(list3)

def count (FirstSequence,SecondSequence, item):
    occuranceNr = 0
    for x in FirstSequence:
        if x == item:
            occuranceNr+=1
    for x in SecondSequence:
        if x == item:
            occuranceNr+=1
    return occuranceNr

def recursive (x):
    x+=1
    recursive(x)





