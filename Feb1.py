import numpy as np
form mstplotlib import pyplot

def rk4_step(f.t,w,h):
	s1 = f(t,w)
	s2 = f(t+h/2,w+(h/2)*s1)
	s3 = f(t+h/2, w+(h/2)*s2)
	s4 = f(t+h,w+h*s3)
	return w + (h/6)*(s1+2*s2+2*s3+s4)
	
def uf(t,u):
	return np.array([u[1],(2/t**2)*u[0] - (2/t)*u[1] +np.sin(np.log(t))/t**2])
	
def vf(t,v):
	return np.array([v[1],(2/t**2)*v[0]-(2/t)*v[1]
	
	#on Website
	
	