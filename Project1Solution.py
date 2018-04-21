#Project1

#Second Order ODE
#y''(x) = x^2 - y'(x) +2
#y(0) =1 y'(0) = 0

import numpy as np
from matplotlib import pyplot

#analyticall solution g(t)
def g(t):
    return -4*np.exp(-t) + (t**3)/3 - t**2 + 4*t + 5

#y' = v
#v'= x^2 -v +2
#def z(t,w):


I = [0,4]

n = 500

h = 4.0/500.0

t = [0]

def Euler(f, g, a, b, y0, n):
    h = (b - a) / float(n)
    g = g(b)

    t = [a]
    w = [y0]

    for i in range(n):
        w.append(w[i] + h * f(t[i], w[i]))
        t.append(t[i] + h)

    err = (g - w[n])

    return w,err


# Trapezoid method to approximate ODE returns global truncaiton erro at last step
def trap(f, g, a, b, y0, n):
    h = (b - a) / float(n)
    g = g(b)

    t = [a]
    w = [y0]
    for i in range(n):
        w.append(w[i] + (h / 2) * (f(t[i], w[i]) + f((t[i] + h), w[i] + h * (f(t[i], w[i])))))
        t.append(t[i] + h)
    err = (g - w[n])

    return w,err

def rk4(f,g,a,b,y0,n):
    t = [0]
    w  =[y0]
    h = (b -a) / float(n)
    g = g(b)
    for i in range(n):
        s1 = f(t[i],w[i])
        s2  =f(t[i]+h/2,w[i] + (h/2 * s1))
        s3 = f(t[i] + h/2, w[i] + (h/2 * s2))
        s4 = f(t[i] + h, w[i] + (h*s3))
        w.append(w[i]+ (h/6)*(s1 + 2*s2 + 2*s3 + s4))
        t.append(t[i] + h)
    err  = (g - w[n])
    return w,err

def Admbash(f,g,a,b,y0,n):
    t = [0]
    w = [0]
    g = g(b)
    h = (b-a) / float(n)
    start = rk4(f,g,a,b,y0,2)
    start[1] = w[0]
    for i in range(1,n):
        w.append(w[i] + h*((3/2)*f(t[i],w[i]) - 1/2 * f(t[i-1],w[i-1])))
        t.append(t[i]+h)

    return w


#graph analyticall solution
y = [1]

for i in range(500):
    t.append(t[i] + h)
    y.append( g(t[i]))


fig,ax = pyplot.subplots()
pyplot.title('Solution on [0,4]')
ax.plot(t,y)
pyplot.xlabel('t')
pyplot.ylabel('y')
pyplot.show()


