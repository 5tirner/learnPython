def ifIn(v):
    if "G" in v:
        return (True)
    return (False)
def ifNot(v):
    if "B" not in v:
        return (False)
    return (True)
def sliceString(string, begin, end):
    return (string[begin:end])
#----------------------------------#
print("Hello My Name Is 'ALEGATOR'")
var = """First,
Second,
Lastest"""
print(var)
print(var[0])
print(len(var), type(len(var)))
var = 'GG'
print('GG' in var)
print(ifIn(var))
print(ifNot(var))
var = "  Good Luck!"
save = sliceString(var, -5, -4)
print(save)
save = var.upper()
print(save)
save = var.lower()
print(save)
save = var.strip()
print(save)
save = var.replace('o', 'u')
print(save)
name = "Messi"
age = 36
all = f"The Great Player Is {name} Enev If He In {age}Yo"
print(all)
myAge = 23
im = "Im {} now"
print(im.format(myAge))
print(bool(2))