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
createListWithConstructor.clear()
print(createListWithConstructor)
createListWithConstructor.insert(0, "Hi")
print(createListWithConstructor)
createListWithConstructor = list((1, 2, 3, 4, 5, 6))
# for n in createListWithConstructor :
#     print(n)
# for i in range(len(createListWithConstructor)) :
#     print(createListWithConstructor[i])

# i = 0
# while i < len(createListWithConstructor) :
#     print(createListWithConstructor[i])
#     i += 1
# [print(x) for x in createListWithConstructor]
lista = [fill for fill in createListWithConstructor if fill % 2 == 0]
print(lista)
lista2 = [364, 4358, 438, 3478, 356784, 453, 4, 3264, 3475, 435, 46, 34]
# lista2.sort(reverse = True)
print(lista2)
def compareStr(a, b) :
    i = j = 0
    while i < len(a) or j < len(b) :
        if (a[i] != b[j]) :
            return ord(a[i]) - ord(b[j])
            # print(ord(a[i]), ord(b[j]))
        i += 1
        j += 1
    return 0
a, b = "ABC", "ABD"
print(compareStr(a, b))
lista3 = lista2.copy()
print(lista3[2:5])