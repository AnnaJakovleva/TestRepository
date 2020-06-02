'''
UserShapeInput = input("Enter the geometrical shape: ")
if UserShapeInput=="triangle":
    TriangleSideLenght= int(input("Please enter triangle side length: "))
    TriangleHeight= int(input("Please enter triangle height: "))
    print("Area of triangle is:" , TriangleSideLenght*TriangleHeight/2)   
    print("Circumference of a triangle is:", 2*TriangleSideLenght+TriangleHeight)

if UserShapeInput=="square":
    SquareSideLength=int(input("Please enter square side length: "))
    print("Area of a square is: ", SquareSideLength*SquareSideLength)
    print("Circumference of a square is: ", 4*SquareSideLength)

if UserShapeInput=="rectangle":
    RectangleFirstSideLenght=int(input("Plese enter rectangle first side lenght: "))
    RectagleSecondSideLenght=int(input("Please enter rectangle second side lenght: "))
    print("Area of a rectangle is: ", RectangleFirstSideLenght*RectagleSecondSideLenght)
    print("Circumference of a rectangle is: ",2*(RectangleFirstSideLenght+RectagleSecondSideLenght))

else:
    print("The entered value is incorrect.")    
'''
'''
firstVariable = True
secondVariable = False
thirdVariable = True

if firstVariable:
    print("This is true")
else:
    print("This is not true") 

if secondVariable or firstVariable:
    print("This is true")  
elif secondVariable and secondVariable and thirdVariable:
    print("This is not true")
else:
    print("Third thing") 

if firstVariable: print("This")


if firstVariable:
    pass 
    print("this")

thisISMyList = ["car", 4 , "blue"]
print(thisISMyList)
print(thisISMyList[1])
print(thisISMyList[-1])
print(thisISMyList[0:3])
print(thisISMyList[:])

thisISMyList.append("dog")
print(thisISMyList)

thisISMyList.remove(4)
print(thisISMyList)

thisISMyList.pop(0)
print(thisISMyList)

del thisISMyList[0]
print(thisISMyList)

del thisISMyList
print(thisISMyList)

thisISMyList.clear()
print(thisISMyList)

thisISMyList.insert(0,"First item")
print(thisISMyList)

thisISMyList.insert(0,"New first item")
print(thisISMyList)

thisIsMySecondlist = thisISMyList
print(thisIsMySecondlist)

thisIsMySecondlist = thisISMyList.copy()
print(thisIsMySecondlist)

thisIsMySecondlist.reverse()
print(thisIsMySecondlist)

print(thisIsMySecondlist.count("First item"))


Write a program that asks for user input (only numbers),
adds that input to a list, then returns to the user the largest number in the list, the smallest number , 
and the sum of the numbers. (The list is only 4 items long).
'''
'''
firstValue = int(input("Enter first numbe "))
secondValue = int(input("Enter second number "))
thirdValue = int(input("Enter third number "))
fourthValue = int(input("Enter fourth number "))


exerciseList =[]
exerciseList.append(firstValue)
exerciseList.append(secondValue)
exerciseList.append(thirdValue)
exerciseList.append(fourthValue)

if exerciseList[0]>exerciseList[1] and exerciseList[0]>exerciseList[2] and exerciseList[0]>exerciseList[3]:
    print("The largest value is ", exerciseList[0])

if exerciseList[1]>exerciseList[0] and exerciseList[1]>exerciseList[2] and exerciseList[1]>exerciseList[3]:
    print("The largest value is ", exerciseList[1])

if exerciseList[2]>exerciseList[0] and exerciseList[2]>exerciseList[1] and exerciseList[2]>exerciseList[3]:
    print("The largest value is ", exerciseList[2])

if exerciseList[3]>exerciseList[0] and exerciseList[3]>exerciseList[1] and exerciseList[3]>exerciseList[2]:
    print("The largest value is ", exerciseList[3])

if exerciseList[0]<exerciseList[1] and exerciseList[0]<exerciseList[2] and exerciseList[0]<exerciseList[3]:
    print("The smallest value is ", exerciseList[0])

if exerciseList[1]<exerciseList[0] and exerciseList[1]<exerciseList[2] and exerciseList[1]<exerciseList[3]:
    print("The smallest value is ", exerciseList[1])

if exerciseList[2]<exerciseList[0] and exerciseList[2]<exerciseList[1] and exerciseList[2]<exerciseList[3]:
    print("The smallest value is ", exerciseList[2])

if exerciseList[3]<exerciseList[0] and exerciseList[3]<exerciseList[1] and exerciseList[3]<exerciseList[2]:
    print("The smallest value is ", exerciseList[3])

sumOfAllNumbers= exerciseList[0]+exerciseList[1]+exerciseList[2]+exerciseList[3]
print(sumOfAllNumbers)

'''
thisIsATuple = ("a", 5, "car")
print(thisIsATuple)

print(thisIsATuple[0])

if "a" in thisIsATuple:
    print("True")

print(len(thisIsATuple))

thisIsMySecondTuple = (1,3,4,10,22,5)
print(max(thisIsMySecondTuple))
print(min(thisIsMySecondTuple))
print(sum(thisIsMySecondTuple))

thisIsMyThirdTuple = thisIsATuple+thisIsMySecondTuple
print(thisIsMyThirdTuple)

thisIsDictionary = {
    "maker":"Dell",
    "color":"gray",
    "year": 2005,
    "price":500
}
print(thisIsDictionary)
print(thisIsDictionary["color"])

thisIsDictionary["RAM"] = 8
print(thisIsDictionary)

thisIsDictionary.pop("year")
print(thisIsDictionary)



