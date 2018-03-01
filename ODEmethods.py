


import numpy as np
import matplotlib as pyplot
import math
import pylab
import scipy as sc



# Euler,trap, Runge, Adams bash


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




def f(t,w):
    return t*w + t**3
def g(t):
    return 3 * math.exp((t**2)/2) - t**2 - 2

print(Euler(f,g,0,1,1,10))

print(trap(f,g,0,1,1,10))

print(rk4(f,g,0,1,1,10))

print(Admbash(f,g,0,1,1,10))










''''	 
def DuffingEQ(alpha,beta,w,gamma,delta):

    return x2 + delta * x1 + alpha * x + beta * x^3 - gamma * math.cos(w*t)
'''
