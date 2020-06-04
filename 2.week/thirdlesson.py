'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
'''
'''
testList = [1, "Hello", 32, "Goodbye","Testing"]

for element in testList:
    print(testList.index(element))
    indexOfOurObject = testList.index(element)
    testList[indexOfOurObject]= "I changed it"
    print(testList)

print(testList)
'''
'''
for whatever in testList:
    print("Hey")

for whatever in range(20):
    if whatever == 10:
        print(whatever)    
'''
'''Make 2 lists with any values, using a for loop print out all values in both lists
'''
'''
firstList=["x","y","z"]
secondList=[1,2,3]

index = 0 

for element in firstList:
    print(firstList[index])
    print(secondList[index])
    index = index + 1
'''

'''
for element in firstList:
    index = firstList.index(element)
    print(firstList[index])
    print(secondList[index])
'''
'''
for element in firstList:
    print(firstList[firstList.index(element)])
    print(secondList[firstList.index(element)])
'''
''' Create a list with any values, 
Make 2 copies of that list with a for loop.
'''
'''
thirdList=[1,2,3]
fourthList=[]
fifthList=[]
for element in thirdList:
    fourthList.append(element)
    fifthList.append(element)
print(fourthList)
print(fifthList)
'''
'''list1=[12,15,32,42,55,75,122,132,150,180,200]
display the numbers that are divisible by 5 and if you find a number greater than 150, stop the loop
'''

list1=[12,15,32,42,55,75,122,132,150,180,200]
for element in list1:
    if element>150:
            break  
    if element%5==0:
        print(element)


        
