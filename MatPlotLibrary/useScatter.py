import matplotlib.pyplot as graphic
import numpy

x = numpy.random.randint(1000, size=(1000))
y = numpy.random.randint(500, size=(1000))
colors = numpy.random.randint(100, size=(1000))
sizes = numpy.random.randint(500, size=(1000))
graphic.title("Colored Points")
graphic.xlabel("HOR")
graphic.ylabel("VER")
graphic.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='nipy_spectral')
graphic.colorbar()
graphic.show()