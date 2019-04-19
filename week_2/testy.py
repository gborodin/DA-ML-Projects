import numpy as np
from numpy import linalg
import pylab
import math
import matplotlib.pyplot as plot


x1 = 1.
x2 = 4.
x3 = 10.
x4 = 15.
y1 = np.sin(x1 / 5.) * np.exp(x1 / 10.) + 5. * np.exp(-x1 / 2.)
y2 = np.sin(x2 / 5.) * np.exp(x2 / 10.) + 5. * np.exp(-x2 / 2.)
y3 = np.sin(x3 / 5.) * np.exp(x3 / 10.) + 5. * np.exp(-x3 / 2.)
y4 = np.sin(x4 / 5.) * np.exp(x4 / 10.) + 5. * np.exp(-x4 / 2.)


print(y1, y2, y3, y4)

A = np.array([[1, 1, 1, 1], [1, 4, 16, 64],[1, 10, 100, 1000], [1,15, 225, 3375],], dtype=float)
b = np.array([y1, y2, y3, y4], dtype=float)
r = linalg.solve(A, b)
print(r[0], r[1], r[2], r[3])

x = np.arange(0, 16, 0.1)
f = np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)
f1 = r[0] + (r[1] * x) + (r[2] * x * x) + (r[3]* x * x * x)
plot.plot(x, f)
plot.plot(x, f1)
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()
# Display
plot.show()