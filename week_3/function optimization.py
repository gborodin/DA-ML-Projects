import numpy as np
import scipy
from scipy import optimize
def f(x):
    return np.sin(x / 5.) * np.exp(x / 10.) + 5. * np.exp(-x / 2.)



def h(x):
    return int(f(x))

x = np.arange(1,30.1,0.1, dtype=float)



bounds = [(1,30)]

print(scipy.optimize.minimize(fun=h, x0=30, method='BFGS'))

print(scipy.optimize.differential_evolution(func=h, bounds=bounds))

