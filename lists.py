aList = ["1", 2, "23", "3"]
print(type(aList))
print(aList)
aList[1] = "5"
print(aList)
print(f"Len Of The List: {len(aList)}")
createListWithConstructor  = list((1, 2, 3, 4))
print(createListWithConstructor)
print(createListWithConstructor[0])
print(createListWithConstructor[-2])
print(createListWithConstructor[1:3])
if 1 in createListWithConstructor:
    print("One Appear In The List")
createListWithConstructor[1:3] = ["10", 11]
print(createListWithConstructor)
createListWithConstructor.insert(0, "GOOD")
print(createListWithConstructor)
createListWithConstructor.append("Bad")
print(createListWithConstructor)
createListWithConstructor.extend(aList)
print(createListWithConstructor)
createListWithConstructor.remove(1) #Delete By Content
print(createListWithConstructor)
createListWithConstructor.pop(-1) #Delete By Index
print(createListWithConstructor)
del createListWithConstructor[-1] #Delete By Index
print(createListWithConstructor)
