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
        z.append(z[i] + h* r(t[i],w[i]))
        w.append(w[i] + h * f(t[i], w[i],z[i]))
        t.append(t[i] + h)



    return t,z,w


# Trapezoid method to approximate second order ODE
def trap(f,r, a, b, w0,z0, n):
    h = (b - a) / float(n)
    z = [z0]
    t = [a]
    w = [w0]
    for i in range(n):
        z.append(z[i] + (h / 2) * (r(t[i], w[i]) + r((t[i] + h), w[i] + h * (r(t[i], w[i])))))
        w.append(w[i] + (h / 2) * (f(t[i], w[i],z[i]) + f((t[i] + h), w[i] + h * (f(t[i], w[i],z[i])),z[i])))
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




fig,ax= pyplot.subplots()
pyplot.title('Solution on [0,1]')

pyplot.xlabel('t')
pyplot.ylabel('y')
t,z,w= Euler(f,r,0 ,1, 0,1, 500)



t,x,v= trap(f,r,0 ,1,0,1, 500)

t,c,p = rk4(f,r,0 ,1, 0,1, 500)
y = [1]
for i in range(500):

    y.append( g(t[i]))


ax.plot(t,z,color = 'red',label = 'Euler')


ax.plot(t,x,color = 'green',label = 'Trap')

ax.plot(t,c,color = 'purple',label ='RK4')

ax.plot(t,y,color = 'aqua',label=' Analyticall Solution')
ax.legend()

Eulererr = [0]
Traperr = [0]
RK4err  =[0]
for i in range(500):
    Eulererr.append(y[i]-z[i])
    Traperr.append(y[i]-x[i])
    RK4err.append(y[i]-c[i])

fig,dx = pyplot.subplots()
pyplot.title('Error')
dx.set_yscale('log')
pyplot.xlabel('t')
pyplot.ylabel('error')
dx.plot(t,np.absolute(Eulererr),color = 'red',label = 'Euler Error')
dx.plot(t,np.absolute(Traperr),color = 'green',label = 'Trap Error')
dx.plot(t,np.absolute(RK4err),color = 'purple',label = 'RK4 Error')
dx.legend()

pyplot.show()



