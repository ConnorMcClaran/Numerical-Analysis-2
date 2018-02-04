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
	
def Euler(f,g,a,b,y0,n,h):
        g = [g(a)]
        
        t = [a]
        w = [y0]
        err = [0]
        for i in range(n):
                print(w[i])
                g.append(g(t[i]))
                w.append(w[i] + h*f(t[i],w[i]))
                t.append(t[i] + h)

        err.append(g[i] - w[i])
        return err



def trap(f,a,b,y0,n):
        h = (b-a) / float(n)
        
        t = [a]
        w = [y0]
        for i in range(n):
                print(w[i])
                w.append(w[i] + (h/2)*(f(t[i],w[i])+ f((t[i]+h), w[i]+ h*(f(t[i],w[i])))))
                t.append(t[i] + h)

        return w,t

def step(k):
        return 0.1 * 2**(-k)


x = np.linspace(0,5,num = 500)
print(x)

def generateh(x,n):
        h = [0]
        for i in range (n):
                
                h.append( step(x[i]))

        return h

h = generateh(x,500)



#for every h[i] I need a err[i] that corresponds with that h-value, 4 iterations

def generr(h,n,f,g):
        err = [0]
        for i in range(n):
                err.append(Euler(f,g,0,1,0,4,h[i])

        return err

print(generr(h,500,f,g))
                        
                           
        


        



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


        










        
