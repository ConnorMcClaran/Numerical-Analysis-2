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
def Euler(f,g,a,b,y0,n):
        h = (b-a)/float(n)
        g = g(b)
        
        t = [a]
        w = [y0]
        
        for i in range(n):
                
                
                w.append(w[i] + h*f(t[i],w[i]))
                t.append(t[i] + h)

        err = (g - w[n])
        
        return err



#Trapezoid method to approximate ODE returns global truncaiton erro at last step
def trap(f,g,a,b,y0,n):
        h = (b-a)/float(n)
        g = g(b)
        
        t = [a]
        w = [y0]
        for i in range(n):
                
                w.append(w[i] + (h/2)*(f(t[i],w[i])+ f((t[i]+h), w[i]+ h*(f(t[i],w[i])))))
                t.append(t[i] + h)
        err = (g - w[n])
        
        return err



#n should vary from 10 to 320
def maken(a,b):
        n = [a]
        x = b-a
        for i in range(x):
                n.append(n[i] + 1)
        return n

n = maken(10,320)

#At n value find the global truncation error
def generr(n,f,g,method,x):
        err = [0]
        for i in range(x):
                err.append(abs(method(f,g,0,1,0,n[i])))

        return err

#print(error)
def genh(n,x):
        h = [0]
        for i in range(x):
                h.append(1/(n[i]))
        return h

error = generr(n,f,g,Euler,310)

h = genh(n,310)

h2 = genh(n,310)

error2  = generr(n,f,g,trap,310)

fig,ax = pyplot.subplots()
ax.plot(h,error,label ='Euler')
ax.plot(h2,error2,label ='Trapezoid')
pyplot.suptitle('Global Truncation Error')
pyplot.title('as a function of h = 0.1 * 2^-k 0<k<5')
pyplot.xscale('log')
pyplot.yscale('log')
ax.set_xlabel('h-value')
ax.set_ylabel('Global Truncation Error')
ax.legend()
pyplot.show()






#PROBLEM 2


# y0 = 0

def g2(x):
        return (math.exp(2*x) -1)/(1+ math.exp(2*x))

def h(t,w):
        return 1 - w**2 + (t*0)


def trap2(f,g,a,b,y0,n,h):
        g = g(b)
        localerr = [0]
        globalerr = [0]
        t = [a]
        w = [y0]
        for i in range(n):
                
                w.append(w[i] + (h/2)*(f(t[i],w[i])+ f((t[i]+h), w[i]+ h*(f(t[i],w[i])))))
                t.append(t[i] + h)
                localerr.append((abs(w[i] - w[i-1])))
                globalerr.append(abs(g-w[i]))
        
        return localerr,globalerr,w



L,G,w = trap2(h,g2,0,1,0,10,0.1)
n = 10
step = [0,1,2,3,4,5,6,7,8,9,10]

print('\n')
print('Problem 2 table of values')
print('------------------------------------------------------------')
print(' w[i]   |   localerror     |       globalerror    |  Step')
print('-------------------------------------------------------------')

for i in range(n+1):
        
        print('%1.6f |   %1.8f    |    %1.8f        | %1.8f ' %
              (w[i], L[i],G[i],step[i]))

              
print('\n')

fig,ax = pyplot.subplots()
ax.plot(step,L,label = 'local error')
ax.plot(step,G, label = 'global error')
pyplot.suptitle('Problem 2 Trapezoid Error')
pyplot.title('h = 0.1')
ax.set_xlabel('step')
ax.set_ylabel('Error')
ax.legend()
pyplot.show()


        










        

