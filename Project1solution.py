


import numpy as np
import matplotlib as pyplot
import math
import pylab

'''
x = np.linspace(-15,15,100) # 100 linearly spaced numbers
y = np.sin(x)/x # computing the values of sin(x)/x

# compose plot
pylab.plot(x,y) # sin(x)/x
pylab.plot(x,y,'co') # same function with cyan dots
pylab.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
pylab.show() # show the plot
'''


def Euler(f,a,b,ya,n):
	 h = (b-a)/float(n)
	 x = a
	 y = ya
	 for i in range(n):
		 y += h*f(x,y)
		 x += h
	 return y

def Euler2(f,a,b,ya,y1a,n):
	 h = (b-a) / float(n)
	 x = a
	 y = ya
	 y1 = y1a
	 for i in range(n):
		  y1 += h * f(x,y,y1)
		  y += h* y1
		  x += h
	 return y

''''	 
def DuffingEQ(alpha,beta,w,gamma,delta):

	return x2 + delta * x1 + alpha * x + beta * x^3 - gamma * math.cos(w*t)
'''
