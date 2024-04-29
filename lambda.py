x = lambda a : a + 10
print(x(10))
x = lambda a, b, c : a * b * c
print(x(1,2,3))

def multupleIt(p):
    return lambda a: a * p

test = multupleIt(2)
print(test(4)) 