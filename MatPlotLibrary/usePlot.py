import matplotlib
import matplotlib.pyplot as mpl

print(matplotlib.__version__)
x = [0,  4, 8, 12, 16, 20]
y = [10, 3, 7, 11, 1 , 15]
x1 = [1, 3, 5, 7, 9]
y1 = [10,3, 7, 11,1]
mpl.subplot(2,1,1)
mpl.plot(x, y)
mpl.plot(x, y, 'o-k', mec='y')
mpl.plot(x1, y1, 'o:y', mec='k')
mpl.xlabel("Horizontal")
mpl.ylabel("Vertical")
mpl.title("Stats", loc="left")
mpl.grid()
mpl.subplot(2,1,2)
mpl.scatter(1,1)
mpl.show()