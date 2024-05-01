import matplotlib.pyplot as window
import numpy
window.title("Random Choice")
window.xlabel("Horizontal")
window.ylabel("Vertical")
numbers = numpy.random.normal(100, 10, 164)
window.hist(numbers)
window.show()