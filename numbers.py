import random

var1 = int(1)
var2 = float(1)
var3 = complex(3)

print(var1,'->', type(var1))
print(var2,'->', type(var2))
print(var3,'->', type(var3))
print('Generate A Random Number:', random.randrange(1, 10))
var3 = float("1")
print(var3,'->', type(var3))
var3 = str(1.0j)
print(var3,'->', type(var3))
