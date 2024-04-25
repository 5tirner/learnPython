import sys
print(sys.version)
if "M" > "H":
    print("T")
x = "Hi"
print(x)
x = 4657437567463576346547698549867965837965897688
x += 1
print(x, "->", type(x))
a = b = c = d = 10
print(a, b, c, d)
arr = ["1", "2", "3", "4"]
a,b,c,d=arr
print(a, b, c, d)
print(a + b + c + d)
print('-----------------------------------------------------------')
def g():
    global think
    think = "smart"
    print(think)
g()
print(think)