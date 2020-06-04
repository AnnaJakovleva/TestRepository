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

for x in homeWorkList:
    for i in range(1,11):
        multiplicationResult=x*i
        print(multiplicationResult)

additionOfMultiplicationList=[]
