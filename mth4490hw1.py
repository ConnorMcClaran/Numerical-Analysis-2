#Connor McClaran
#MTH4490 HW1


import math
import numpy as np
from matplotlib import pyplot

#y'(t) = 4t - 2y(t) d'Alembert's equation


#general solution

def g(t):
        return math.exp(-2*t) + 2*t - 1


def f(t,w):
	return 4*t - 2*w

#Euler approximation to ODE returns global truncation error at the last step	
def Euler(f,g,a,b,y0,n,h):
        g = g(a)
        
        t = [a]
        w = [y0]
        
        for i in range(n):
                
                
                w.append(w[i] + h*f(t[i],w[i]))
                t.append(t[i] + h)

        err = (g - w[n])
        return err


#Trapezoid method to approximate ODE returns global truncaiton erro at last step
def trap(f,g,a,b,y0,n,h):
        g = g(a)
        
        t = [a]
        w = [y0]
        for i in range(n):
                
                w.append(w[i] + (h/2)*(f(t[i],w[i])+ f((t[i]+h), w[i]+ h*(f(t[i],w[i])))))
                t.append(t[i] + h)
        err = (g - w[n])
        return err

# h as a function of k
def step(k):
        return 0.1 * 2**(-k)

# generate 500 k values from  0 to 5
x = np.linspace(0,5,num = 500)

#Function to create h array
def generateh(x,n):
        h = [0]
        for i in range (n):
                
                h.append( step(x[i]))

        return h

h = generateh(x,500)


#At h value find the global truncation error
def generr(h,n,f,g,method):
        err = [0]
        for i in range(n):
                err.append(abs(method(f,g,0,1,0,4,h[i])))

        return err



error = generr(h,500,f,g,Euler)
                        
                           


#Euler plot

fig,ax = pyplot.subplots()
ax.plot(h,error)
pyplot.suptitle('Euler Global Truncation Error')
pyplot.title('as a function of h = 0.1 * 2^-k 0<k<5')
pyplot.xscale('log')
pyplot.yscale('log')
ax.set_xlabel('h-value')
ax.set_ylabel('Global Truncation Error')
pyplot.show()




#now for trap method
error2  = generr(h,500,f,g,trap)

fig,ax = pyplot.subplots()
ax.plot(h,error2)
pyplot.suptitle('Trapezoid Global Truncation Error')
pyplot.title('as a function of h = 0.1 * 2^-k 0<k<5')
pyplot.xscale('log')
pyplot.yscale('log')
ax.set_xlabel('h-value')
ax.set_ylabel('Global Truncation Error')
pyplot.show()



        



'''
print(trap(f,0,1,0,4))

# y0 = 1

def h(t,w):
        return 1 - w**2 + (t*0)


#test failure
print(trap(h,0,1,1,10))





#Test genral solution

print(g(1))

#Test Euler at y0 = 0 with 4  interations
'''
#print(Euler(f,g,0,1,0,4))
'''
#print(Euler(f,0,1,0,10))

#print(Euler(f,0,1,0,20))

#print(Euler(f,0,1,0,50))
'''


        










        
