#Connor McClaran
#MTH4490 HW1
import math

#y'(t) = 4t - 2y(t) d'Alembert's equation


#general solution

def g(t):
        return math.exp(-2*t) + 2*t - 1


def f(t,w):
	return 4*t - 2*w
	
def Euler(f,a,b,y0,n):
        h = (b-a)/float(n)
        x = a
        y = y0
        for i in range(n):
                
                y += h*f(x,y)
                x += h
        return y

#Test genral solution

print(g(1))

#Test Euler at y0 = 0 with 4  interations

print(Euler(f,0,1,0,4))

#print(Euler(f,0,1,0,10))

#print(Euler(f,0,1,0,20))

#print(Euler(f,0,1,0,50))










        
