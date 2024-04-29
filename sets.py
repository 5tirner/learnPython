set1 = {"1", "2", "3"}
print(set1)
setUnduplicated = {1,1,1,1,1,1,1,1,1,1}
print(setUnduplicated)
print(type(set1))
setConstructor = set(("a", "b", "c"))
print(setConstructor)
print(type(setConstructor))
setConstructor.add('d')
print(setConstructor)
setConstructor.update(set1)
print(setConstructor)
setConstructor.remove('1')
print(setConstructor)
#----------------------------