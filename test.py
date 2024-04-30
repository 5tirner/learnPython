import matplotlib
import matplotlib.pyplot as mpl
import numpy as ny

print(matplotlib.__version__)
x, y = ny.array([0, 4]), ny.array([0, 200])
mpl.plot(x, y)
mpl.show()