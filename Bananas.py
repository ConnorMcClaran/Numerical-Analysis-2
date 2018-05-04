import numpy as np
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

#Connor McClaran
#Optimizers
#gss
#Newton method
#Gradient Decent

#f(x,y = (1-x**2) + 100*(y-x**2)**2


def f(x,y):
    return (1 - x**2) + 100*(((y - x**2))**2)
#df/dx
def fpx1(x,y):
    return -2*x + 400*x**3 - 400*x*y
#df/dy
def fpy1(x,y):
    return 200*y + 200*x**2

y = np.linspace(0.0,2.0,100)
x = np.linspace(-2.0,2.0,100)

z = np.zeros((100,100))
for i in range(100):
    for j in range(100):

        z[i,j] = f(x[i],y[j])

X,Y = np.meshgrid(x,y)


fig  = pyplot.figure()

banana = fig.add_subplot(111,projection = '3d')
pyplot.title('f(x,y) on x[-2.0,2.0] y[0,2.0]')
banana.plot_surface(X,Y,z)

banana.set_xlabel('x')
pyplot.legend()
banana.set_ylabel('y')
banana.set_zlabel('f(x,y)')
pyplot.show()



#Minimize with Golden Section Search

def gss(a,b,f,tol):
    g = (np.sqrt(5.0)-1.0)/2.0
    k = np.int(np.ceil(np.log(1.0*tol/(b-a))/np.log(g)))
    x1 = a + (1.0-g)*(b-a)
    x2 = a + g*(b-a)
    f1 = f(x1)
    f2 = f(x2)
    for i in range(k):
        if f1 < f2:
            b=x2
            x2=x1
            x1=a+(1.0-g)*(b-a)
            f2=f1
            f1=f(x1)
        else:
            a=x1
            x1=x2
            x2=a+g*(b-a)
            f1=f2
            f2=f(x2)
    return (a+b)/2.0

def bisection(x1,x2,y1,y2,fpx1,tol):
    fa = f(x1,y1); fb = f(x2,y2)
    if fa*fb > 0.0:
        print("Error")
    k = 0
    while abs(x1-x2) > tol:
        if fa == 0.0:
            return x1

        if fb == 0.0:
            return x2

        c = (x1+x2)/(2.0)
        fc = f(c,y1)

        if fa*fc < 0.0:
            x2 = c
            fb = fc
        else:
            x1 = c
            fa = fc
        k = k+1
    return (x2+x1)/2.0

r = bisection(-2.0,0.0,0,2.0,f,0.5*10**-5)

#x = gss(I[0],I[1],f,0.5*10**-5)
'''
print(r)
print(f(r,0))
#print(x)
'''
