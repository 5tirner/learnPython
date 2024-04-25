def ifIn(v):
    if "G" in v:
        return (True)
    return (False)
def ifNot(v):
    if "B" not in v:
        return (False)
    return (True)
def sliceString(string, begin, end):
    if begin > end:
        return ""
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
var = "egnjkfdvbfdjkbkjfdhbj vjk bfdjkvjubfdv ndcjkv bfdjbvf"
save = sliceString(var, 6, len(var)+1000)
print(save)