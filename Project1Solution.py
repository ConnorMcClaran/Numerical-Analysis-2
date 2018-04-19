#Project1

#Second Order ODE
#y''(x) = x^2 - y'(x) +2
#y(0) =1 y'(0) = 0

import numpy as np

#analyticall solution g(t)
def g(t):
    return -4*np.exp(-t) + (t**3)/3 - t**2 + 4*t + 5

