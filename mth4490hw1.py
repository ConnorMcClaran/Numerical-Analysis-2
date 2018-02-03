#Connor McClaran
#MTH4490 HW1


import math
import numpy as np
import matplotlib as pyplot

#y'(t) = 4t - 2y(t) d'Alembert's equation


#general solution

def g(t):
        return math.exp(-2*t) + 2*t - 1


def f(t,w):
	return 4*t - 2*w
	
def Euler(f,a,b,y0,n):
        
        h = (b-a)/float(n)
        t = [a]
        w = [y0]
        for i in range(n):
                print(w[i])
                w.append(w[i] + h*f(t[i],w[i]))
                t.append(t[i] + h)
        return w,t



def trap(f,a,b,y0,n):
        h = (b-a) / float(n)
        
        t = [a]
        w = [y0]
        for i in range(n):
                print(w[i])
                w.append(w[i] + (h/2)*(f(t[i],w[i])+ f((t[i]+h), w[i]+ h*(f(t[i],w[i])))))
                t.append(t[i] + h)

        return w,t






#print(trap(f,0,1,0,4))
'''
# y0 = 1

def h(t,w):
        return 1 - w**2 + (t*0)


#test failure
print(trap(h,0,1,1,10))





#Test genral solution

print(g(1))

#Test Euler at y0 = 0 with 4  interations
'''
print(Euler(f,0,1,0,4))
'''
#print(Euler(f,0,1,0,10))

#print(Euler(f,0,1,0,20))

#print(Euler(f,0,1,0,50))
'''


        










        
