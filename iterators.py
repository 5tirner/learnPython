tuple1 = ("1", "2", "3", "4")
it = iter(tuple1)
print(it)
print(next(it))
print(next(it))
print(next(it))
dict1 = dict(name='zakaria', age=23)
it = iter(dict1)
print(next(it))
print(next(it))
s = 'abc'
ss = 'bcd'
t = int(ord(s[0])) - int(ord(ss[0]))