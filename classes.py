class test:
    def __init__(self):
        a = "Defualt"
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"Test Class With An Attribuite a = {self.a}"
obj = test("hghj")
print(obj.a)
obj.a = 55555
print(obj.a)
print(obj)
print(test("Seee").a)
############################################################
class Base:
    def __init__(self, string):
        self.newStr = string
        self.lista = list(())
        for x in string:
            self.lista.append(ord(x))
    def __str__(self):
        return str(self.lista)
    def printRealVal(self):
        return self.newStr
class Child(Base):
    def __init__(self, string, number):
        super().__init__(string)
        self.save = number
    def getNumber(self):
        return self.save
obj = Base("Good")
print(obj)
print(obj.printRealVal())
obj = Child("Bad", 55)
print(obj)
print(obj.printRealVal())
print(obj.getNumber())