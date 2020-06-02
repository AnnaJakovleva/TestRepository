inputListOne = []
firstValueListOne=int(input("Enter first value: "))
secondValueListOne=int(input("Enter second value: "))
thirdValueListOne=int(input("Enter third value: "))
fourthValueListOne=int(input("Enter fourth value: "))
fifthValueListOne=int(input("Enter fifth value: "))
sixthValueListOne=int(input("Enter sixth value: "))
seventhValueListOne=int(input("Enter seventh value: "))
eighthValueListOne=int(input("Enter eighth value: "))
ninthValueListOne=int(input("Enter ninth value: "))
tenthValueListOne=int(input("Enter tenth value: "))

inputListOne.append(firstValueListOne,
                    secondValueListOne,
                    thirdValueListOne,
                    fourthValueListOne,
                    fifthValueListOne,
                    sixthValueListOne,
                    seventhValueListOne,
                    eighthValueListOne,
                    ninthValueListOne,
                    tenthValueListOne)

outputListOne=[firstValueListOne*firstValueListOne,secondValueListOne*secondValueListOne,
thirdValueListOne*thirdValueListOne,fourthValueListOne*fourthValueListOne,
fifthValueListOne*fifthValueListOne,sixthValueListOne*sixthValueListOne,
seventhValueListOne*seventhValueListOne,eighthValueListOne*eighthValueListOne,
ninthValueListOne*ninthValueListOne,tenthValueListOne*tenthValueListOne]
outputListOne.reverse()
print(outputListOne)

inputListTwo=[]
if len(outputListOne)>0:
    firstValueListTwo=int(input("Enter first value list two: "))
    if firstValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3] or outputListOne[4] or outputListOne[5] or outputListOne[6] or outputListOne[7] or outputListOne[8] or outputListOne[9]:
        inputListTwo.append(firstValueListTwo)
        outputListOne.remove(firstValueListTwo)
        print(outputListOne)
        print(inputListTwo)

if len(outputListOne)>0:
    secondValueListTwo=int(input("Enter second value list two: "))
    if secondValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3] or outputListOne[4] or outputListOne[5] or outputListOne[6] or outputListOne[7] or outputListOne[8]:
        inputListTwo.append(secondValueListTwo)
        outputListOne.remove(secondValueListTwo) 
        print(outputListOne)
        print(inputListTwo)

if len(outputListOne)>0:
    thirdValueListTwo=int(input("Enter third value list two: "))
    if thirdValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3] or outputListOne[4] or outputListOne[5] or outputListOne[6] or outputListOne[7]:
        inputListTwo.append(thirdValueListTwo)
        outputListOne.remove(thirdValueListTwo) 
        print(outputListOne)
        print(inputListTwo)

if len(outputListOne)>0:
    fourthValueListTwo=int(input("Enter fourth value list two: "))
    if fourthValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3] or outputListOne[4] or outputListOne[5] or outputListOne[6]:
        inputListTwo.append(fourthValueListTwo)
        outputListOne.remove(fourthValueListTwo) 
        print(outputListOne)
        print(inputListTwo)

if len(outputListOne)>0:
    fifthValueListTwo=int(input("Enter fifth value list two: "))
    if fifthValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3] or outputListOne[4] or outputListOne[5]:
        inputListTwo.append(fifthValueListTwo)
        outputListOne.remove(fifthValueListTwo) 
        print(outputListOne)
        print(inputListTwo)        

if len(outputListOne)>0:
    sixthValueListTwo=int(input("Enter sixth value list two: "))
    if sixthValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3] or outputListOne[4]:
        inputListTwo.append(sixthValueListTwo)
        outputListOne.remove(sixthValueListTwo) 
        print(outputListOne)
        print(inputListTwo)

if len(outputListOne)>0:
    seventhValueListTwo=int(input("Enter seventh value list two: "))
    if seventhValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2] or outputListOne[3]:
        inputListTwo.append(seventhValueListTwo)
        outputListOne.remove(seventhValueListTwo) 
        print(outputListOne)
        print(inputListTwo)        

if len(outputListOne)>0:
    eighthValueListTwo=int(input("Enter eighth value list two: "))
    if seventhValueListTwo==outputListOne[0] or outputListOne[1] or outputListOne[2]:
        inputListTwo.append(eighthValueListTwo)
        outputListOne.remove(eighthValueListTwo) 
        print(outputListOne)
        print(inputListTwo)     

if len(outputListOne)>0:
    ninthValueListTwo=int(input("Enter ninth value list two: "))
    if ninthValueListTwo==outputListOne[0] or outputListOne[1]:
        inputListTwo.append(ninthValueListTwo)
        outputListOne.remove(ninthValueListTwo) 
        print(outputListOne)
        print(inputListTwo)  

if len(outputListOne)>0:
    tenthValueListTwo=int(input("Enter tenth value list two: "))
    if tenthValueListTwo==outputListOne[0]:
        inputListTwo.append(tenthValueListTwo)
        outputListOne.remove(tenthValueListTwo)
        print(inputListTwo)


