dictionary = {
    "name": "Zakaria",
    "age": 23
}
print(dictionary)
print(type(dictionary))
print(dictionary["name"])
dictConstructor = dict(login = "zasabri", age = 23, status = "dbCEO")
print(dictConstructor)
print(dictConstructor.keys())
dictConstructor["status"] = "3 7"
print(dictConstructor)
print(dictConstructor.values())
print(dictConstructor.items())
dictConstructor.update({"name": "Zakaria Sabri"})
print(dictConstructor.items())
dictConstructor.pop("status")
print(dictConstructor.items())
nestedDict = {
    "Person1":
    {
        "name": "Zakaria",
    },
    "Person2":
    {
        "name": "Sabri",
    },
}
print(nestedDict["Person1"].items())
nestedDict["Person1"].update({"Age": 23})
print(nestedDict["Person1"].items())
print(nestedDict)
nestedDict.update({"Person3":{"name": "Simo"}})
print(nestedDict)
