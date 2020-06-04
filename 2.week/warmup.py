'''
Given the list y = [6,4,2] add the items 12, 8. Then change the 2nd item of the list to 3.
Repeat this process for a dictionary . The key values in the dictionary should be named:
lowest, second lowest, medium, highest, the highest 
'''
listY = [6,4,2]
listY.append(12)
listY.append(8)
print(listY[1])
listY[1]=3
print(listY)

lowestValue= min(listY)
highestValue=max(listY)

dictionaryY={
    "lowest":lowestValue,
    "second lowest":4,
    "medium":6,
}

dictionaryY["highest"]=8
dictionaryY["the highest"]=highestValue
print(dictionaryY)

dictionaryY["second lowest"]=3
print(dictionaryY)