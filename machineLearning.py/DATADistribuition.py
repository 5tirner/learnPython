import numpy
import matplotlib.pyplot as window
import scipy.stats as st
import math

numbers = numpy.random.uniform(5, size=(250))
y = numpy.random.randint(100, size=(250))
front = numpy.random.uniform(0.1, 0.3, 250)
colors = numpy.random.randint(250, size=(250))
sizes = numpy.random.randint(1000, size=(250))
index = 1
for n in numbers:
    print(f"Number {index}: {n}")
    index+=1
window.title("Pie Data Distribution", loc="left")
window.pie(numbers, startangle=0, explode=front, shadow=True)
window.show()
window.title("Hist Data Distribution", loc="left")
window.hist(numbers)
window.show()
window.title("Bar Data Distribution", loc="left")
window.bar(numbers, numbers, width=0.3)
window.show()
window.title("Plot Data Distribution", loc="left")
window.plot(numbers, y, c='k')
window.show()
window.title("Scatter Data Distribution", loc="left")
window.scatter(numbers, y, c=colors, s=sizes, alpha=0.2, cmap='nipy_spectral')
window.show()