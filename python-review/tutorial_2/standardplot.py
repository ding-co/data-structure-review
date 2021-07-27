# Package install: pip3 install matplotlib

from matplotlib import pyplot
import numpy as np

x = np.linspace(0, 20, 100)
pyplot.plot(x, np.sin(x))
pyplot.show()