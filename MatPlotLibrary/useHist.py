import matplotlib.pyplot as window
import numpy
window.title("Random Choice")
window.xlabel("Horizontal")
window.ylabel("Vertical")
x = [1,2,3,4,5,6,7,8,9,1,1,3,3,3,3,3,3,10]
window.hist(x)
window.show()