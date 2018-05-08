#Project1

#Second Order ODE
#y''(x) = x^2 - y'(x) +2y
#y(0) =1 y'(0) = 0

import numpy as np
from matplotlib import pyplot

#analyticall solution g(t)
def g(t):
    return ((-5.0/12.0)+(7.0/4.0))*np.exp(t) + (5.0/12.0)* np.exp(-2*t) - (t**2/2.0) - t/2.0 - 3.0/4.0

#y' = v
#v'= x^2 -v +2y
def f(t,w,z):
    return t**2 -w + 2*z

def r(t,w):
    return w

#Euler Method for Secod Order ODE
def Euler(f ,r, a, b, w0,z0, n):
    h = (b - a) / float(n)
    z = [z0]
    t = [a]
    w = [w0]

    for i in range(n):
        z.append(z[i] + h* w[i])
        w.append(w[i] + h * f(t[i], w[i],z[i+1]))
        t.append(t[i] + h)



    return t,z,w


# Trapezoid method to approximate second order ODE
def trap(f,r, a, b, w0,z0, n):
    h = (b - a) / float(n)
    z = [z0]
    t = [a]
    w = [w0]
    for i in range(n):
        z.append(z[i] + (h / 2) * ( w[i] + w[i] + h*w[i] ))
        w.append(w[i] + (h / 2) * (f(t[i], w[i],z[i+1]) + f((t[i] + h), w[i] + h * (f(t[i], w[i],z[i+1])),z[i+1])))
        t.append(t[i] + h)


    return t,z,w
#RK4 Second order ODE
def rk4(f,r,a,b,w0,z0,n):
    t = [0]
    z=[z0]
    w  =[w0]
    h = (b -a) / float(n)
    for i in range(n):
        s1 = f(t[i],w[i],z[i])
        k1 = r(t[i],w[i])
        s2  =f(t[i]+h/2,w[i] + (h/2 * s1),z[i])
        k2  =r(t[i]+h/2,w[i] + (h/2 * k1))
        s3 = f(t[i] + h/2, w[i] + (h/2 * s2),z[i])
        k3 = r(t[i] + h/2, w[i] + (h/2 * k2))
        s4 = f(t[i] + h, w[i] + (h*s3),z[i])
        k4 = r(t[i] + h, w[i] + (h*k3))
        w.append(w[i]+ (h/6)*(s1 + 2*s2 + 2*s3 + s4))
        z.append(z[i]+ (h/6)*(k1 + 2*k2 + 2*k3 + k4))
        t.append(t[i] + h)

    return t,z,w
'''
def newton(x0,w,z,h,tol):
    def g(x,w,z,h):
        return x - (w + h*(x**2-w + 2*z))
    def gp(x,h):
        return 1 - 2*h*x
    x = x0 - g(x0,w,z,h)/gp(x0,h)
    while abs(x-x0) > tol:
        x0 = x
        x = x0 - g(x0,w,z,h)/gp(x0,h)
    return x

def backEuler(f,w0,z0,h,n,tol):
    w = [w0]
    z = [z0]
    t = np.arange(0,n,h)

    for i in range(50):
        zero = newton(w[i],w[i],z[i],h,tol)
        w.append(w[i]+h*f(t[i+1],w[i],z[i]))
        z.append(z[i] + h* w[i])

    return t,z
'''

fig,ax= pyplot.subplots()
pyplot.title('Solution on [0,1]')

pyplot.xlabel('t')
pyplot.ylabel('y')
#t,m = backEuler(f,0,1,0.01,100,0.5*10**-2)
t,z,w= Euler(f,r,0 ,1, 0,1, 100)



t,x,v= trap(f,r,0 ,1,0,1, 100)

t,c,p = rk4(f,r,0 ,1, 0,1, 100)
y = [1]
for i in range(100):

    y.append( g(t[i]))

#ax.plot(t,m,color = 'yellow',label = 'BackwardEuler')

ax.plot(t,z,color = 'red',label = 'Euler')


ax.plot(t,x,color = 'green',label = 'Trap')

ax.plot(t,c,color = 'purple',label ='RK4')

ax.plot(t,y,color = 'aqua',label=' Analyticall Solution')
ax.legend()

#backEulererr = [0]
Eulererr = [0]
Traperr = [0]
RK4err  =[0]
for i in range(100):
    Eulererr.append(np.absolute(y[i]-z[i]))
    Traperr.append(np.absolute(y[i]-x[i]))
    RK4err.append(np.absolute(y[i]-c[i]))
    #backEulererr.append(np.absolute(y[i] - m[i]))



fig,dx = pyplot.subplots()
pyplot.title('Error h = 0.01')
dx.set_yscale('log')
pyplot.xlabel('t')
pyplot.ylabel('error')
#dx.plot(t,(backEulererr),color = 'yellow',label = 'backEuler Error')
dx.plot(t,(Eulererr),color = 'red',label = 'Euler Error')
dx.plot(t,(Traperr),color = 'green',label = 'Trap Error')
dx.plot(t,(RK4err),color = 'purple',label = 'RK4 Error')
dx.legend()

pyplot.show()



t,z,w= Euler(f,r,0 ,1, 0,1, 1000)



t,x,v= trap(f,r,0 ,1,0,1, 1000)

t,c,p = rk4(f,r,0 ,1, 0,1, 1000)
y = [1]
for i in range(1000):

    y.append( g(t[i]))



Eulererr = [0]
Traperr = [0]
RK4err  =[0]
for i in range(1000):
    Eulererr.append(np.absolute(y[i]-z[i]))
    Traperr.append(np.absolute(y[i]-x[i]))
    RK4err.append(np.absolute(y[i]-c[i]))



fig,ex = pyplot.subplots()
pyplot.title('Error h = 0.001')
ex.set_yscale('log')
pyplot.xlabel('t')
pyplot.ylabel('error')
ex.plot(t,(Eulererr),color = 'red',label = 'Euler Error')
ex.plot(t,(Traperr),color = 'green',label = 'Trap Error')
ex.plot(t,(RK4err),color = 'purple',label = 'RK4 Error')
ex.legend()

pyplot.show()


t,z,w= Euler(f,r,0 ,1, 0,1, 10000)



t,x,v= trap(f,r,0 ,1,0,1, 10000)

t,c,p = rk4(f,r,0 ,1, 0,1, 10000)
y = [1]
for i in range(10000):

    y.append( g(t[i]))



Eulererr = [0]
Traperr = [0]
RK4err  =[0]
for i in range(10000):
    Eulererr.append(np.absolute(y[i]-z[i]))
    Traperr.append(np.absolute(y[i]-x[i]))
    RK4err.append(np.absolute(y[i]-c[i]))



fig,ex = pyplot.subplots()
pyplot.title('Error h = 0.0001')
ex.set_yscale('log')
pyplot.xlabel('t')
pyplot.ylabel('error')
ex.plot(t,(Eulererr),color = 'red',label = 'Euler Error')
ex.plot(t,(Traperr),color = 'green',label = 'Trap Error')
ex.plot(t,(RK4err),color = 'purple',label = 'RK4 Error')
ex.legend()

pyplot.show()


t,z,w= Euler(f,r,0 ,1, 0,1, 100000)



t,x,v= trap(f,r,0 ,1,0,1, 100000)

t,c,p = rk4(f,r,0 ,1, 0,1, 100000)
y = [1]
for i in range(100000):

    y.append( g(t[i]))



Eulererr = [0]
Traperr = [0]
RK4err  =[0]
for i in range(100000):
    Eulererr.append(np.absolute(y[i]-z[i]))
    Traperr.append(np.absolute(y[i]-x[i]))
    RK4err.append(np.absolute(y[i]-c[i]))



fig,ex = pyplot.subplots()
pyplot.title('Error h = 0.00001')
ex.set_yscale('log')
pyplot.xlabel('t')
pyplot.ylabel('error')
ex.plot(t,(Eulererr),color = 'red',label = 'Euler Error')
ex.plot(t,(Traperr),color = 'green',label = 'Trap Error')
ex.plot(t,(RK4err),color = 'purple',label = 'RK4 Error')
ex.legend()

pyplot.show()


t,z,w= Euler(f,r,0 ,1, 0,1, 10000000)



t,x,v= trap(f,r,0 ,1,0,1, 10000000)

t,c,p = rk4(f,r,0 ,1, 0,1, 10000000)
y = [1]
for i in range(10000000):

    y.append( g(t[i]))



Eulererr = [0]
Traperr = [0]
RK4err  =[0]
for i in range(10000000):
    Eulererr.append(np.absolute(y[i]-z[i]))
    Traperr.append(np.absolute(y[i]-x[i]))
    RK4err.append(np.absolute(y[i]-c[i]))



fig,ex = pyplot.subplots()
pyplot.title('Error h = 0.0000001')
ex.set_yscale('log')
pyplot.xlabel('t')
pyplot.ylabel('error')
ex.plot(t,(Eulererr),color = 'red',label = 'Euler Error')
ex.plot(t,(Traperr),color = 'green',label = 'Trap Error')
ex.plot(t,(RK4err),color = 'purple',label = 'RK4 Error')
ex.legend()

pyplot.show()
