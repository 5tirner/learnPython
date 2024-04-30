class one:
    def get():
        return 1
class two:
    def get():
        return 2
nbr1, nbr2 = one, two
for i in (nbr1, nbr2):
    print(i.get())