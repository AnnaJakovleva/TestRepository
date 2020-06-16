homeWorkList=[]
firstValue=int(input("Enter first number "))
secondValue = int(input("Enter second number "))
thirdValue = int(input("Enter third number "))
fourthValue = int(input("Enter fourth number "))
fifthValue = int(input("Enter fifth number "))
sixthValue = int(input("Enter sixth number "))

homeWorkList.append(firstValue)
homeWorkList.append(secondValue)
homeWorkList.append(thirdValue)
homeWorkList.append(fourthValue)
homeWorkList.append(fifthValue)
homeWorkList.append(sixthValue)

print(homeWorkList)

multiplicationListOne=[]
multiplicationListTwo=[]
multiplicationListThree=[]
multiplicationListFour=[]
multiplicationListFive=[]
multiplicationListSix=[]

for x in homeWorkList:
    for i in range(1,11):
        multiplicationResult=x*i
        print(multiplicationResult)
        if len(multiplicationListOne)<10:
            multiplicationListOne.append(multiplicationResult)
        elif len(multiplicationListTwo)<10:
            multiplicationListTwo.append(multiplicationResult)
        elif len(multiplicationListThree)<10:
            multiplicationListThree.append(multiplicationResult)
        elif len(multiplicationListFour)<10:
            multiplicationListFour.append(multiplicationResult)
        elif len(multiplicationListFive)<10:
            multiplicationListFive.append(multiplicationResult)
        elif len(multiplicationListSix)<10:
            multiplicationListSix.append(multiplicationResult)


print(multiplicationListOne)
print(multiplicationListTwo)
print(multiplicationListThree)
print(multiplicationListFour)
print(multiplicationListFive)
print(multiplicationListSix)

sumOFValuesVariable=0
for x in multiplicationListOne:
    if multiplicationListOne.index(x)==0:
        sumOFValuesVariable=x
        continue
    sumOFValuesVariable= sumOFValuesVariable+x
    print(sumOFValuesVariable)

sumOFValuesVariable=0
for x in multiplicationListTwo:
    if multiplicationListTwo.index(x)==0:
        sumOFValuesVariable=x
        continue
    sumOFValuesVariable= sumOFValuesVariable+x
    print(sumOFValuesVariable)

sumOFValuesVariable=0
for x in multiplicationListThree:
    if multiplicationListThree.index(x)==0:
        sumOFValuesVariable=x
        continue
    sumOFValuesVariable= sumOFValuesVariable+x
    print(sumOFValuesVariable)

sumOFValuesVariable=0
for x in multiplicationListFour:
    if multiplicationListFour.index(x)==0:
        sumOFValuesVariable=x
        continue
    sumOFValuesVariable= sumOFValuesVariable+x
    print(sumOFValuesVariable)   

sumOFValuesVariable=0
for x in multiplicationListFive:
    if multiplicationListFive.index(x)==0:
        sumOFValuesVariable=x
        continue
    sumOFValuesVariable= sumOFValuesVariable+x
    print(sumOFValuesVariable) 

sumOFValuesVariable=0
for x in multiplicationListSix:
    if multiplicationListSix.index(x)==0:
        sumOFValuesVariable=x
        continue
    sumOFValuesVariable= sumOFValuesVariable+x
    print(sumOFValuesVariable) 
else:
    print("Done ")

    

