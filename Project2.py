import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize
import time
#Connor McClaran
#Optimizers
#Gradient Descent
#Newton method


#f(x,y = (1-x**2) + 100*(y-x**2)**2


def f(x,y):

    return (1 - x)**2 + 100*(((y - x**2))**2)
#df/dx
def fpx1(x,y):
    return -2 * (1-x) - 400 * (y - x**2) * x
#df/dy
def fpy1(x,y):
    return 200*(y - x**2)
def J(x,y):
    return np.array([fpx1(x,y),fpy1(x,y)]).reshape((2,1))
def H(x,y):
    return [[1200*x**2 - 400*y -2,-400*x],[400*x,200]]


y = np.linspace(0.0,2.0,100)
x = np.linspace(-2.0,2.0,100)

z = np.zeros((100,100))
for i in range(100):
    for j in range(100):

        z[i,j] = f(x[i],y[j])

X,Y = np.meshgrid(x,y)

'''
fig  = pyplot.figure()

banana = fig.add_subplot(111,projection = '3d')
pyplot.title('f(x,y) on x[-2.0,2.0] y[0,2.0]')
banana.plot_surface(X,Y,z)

banana.set_xlabel('x')
pyplot.legend()
banana.set_ylabel('y')
banana.set_zlabel('f(x,y)')
pyplot.show()
'''
def NewtonsMin(x1,x2,y1,y2,tol):
    for W in [[x1,x2], [y1,y2]]:
        s = np.linalg.solve(np.multiply(-1,H(W[0],W[1]),J(W[0],W[1])))
        while np.linalg.norm(s)> tol:
            W += s
            s = np.linalg.solve(np.multiply(-1,H(W[0],W[1]),J(W[0],W[1])))
        return W



def Gradientdescent(f,J,x0,y0,h,tol):
    count = 0
    val = []
    x = np.array([0,0]).reshape((2,1))
    x_new = np.array([x0,y0]).reshape((2,1))
    print(x_new)
    start = time.time()
    while np.linalg.norm(x - x_new)> tol:

        x = x_new

        x_new = x - h * J(x[0],x[1])
        val.append(f(x_new[0],x_new[1]))
        count = count +1
    r = f(x[0],x[1])
    end = time.time()
    length = end -start
    return count,x_new,r,length

def Gradientdescent2(f,J,x0,y0,h,tol):
    count = 0
    val = []
    x = np.array([0,0]).reshape((2,1))
    x_new = np.array([x0,y0]).reshape((2,1))
    print(x_new)
    start = time.time()
    while np.linalg.norm(x - x_new)> tol:

        x = x_new

        x_new = x - h * J(x[0],x[1])
        h = h*(1/(2.0))
        val.append(f(x_new[0],x_new[1]))
        count = count +1
    r = f(x[0],x[1])
    end = time.time()
    length = end - start
    return count,x_new,r,length

def Gradientdescent3(f,J,x0,y0,h,a,B,tol):
    count = 0
    x = np.array([0,0]).reshape((2,1))
    x_new = np.array([x0,y0]).reshape((2,1))
    print(x_new)
    start = time.time()
    while np.linalg.norm(x - x_new) > tol:

        x = x_new

        x_new = x - h * J(x[0],x[1])

        c = 0

        while (f(x_new[0],x_new[1])) > (f(x[0],x[1]) +  (h/(2.0)) * np.linalg.norm((J(x[0],x[1])))):
            h = B * h
            c = c +1
            if c > 8:
                break
        count = count +1
    r = f(x[0],x[1])
    end = time.time()
    length = end -start
    return count,x_new,r,length


#2,2
r1 = Gradientdescent(f,J,2.0,2.0,0.001,0.5*10**-5)
print(r1)

z1 = Gradientdescent2(f,J,2.0,2.0,0.001,0.5*10**-5)
print(z1)

x1 = Gradientdescent3(f,J,2.0,2.0,0.001,0.1,0.5,0.5*10**-5)
print(x1)


#-2,2
r2 = Gradientdescent(f,J,-2.0,2.0,0.001,0.5*10**-5)
print(r2)

z2 = Gradientdescent2(f,J,-2.0,2.0,0.001,0.5*10**-5)
print(z2)

x2 = Gradientdescent3(f,J,-2.0,2.0,0.001,0.1,0.5,0.5*10**-5)
print(x2)

#-2,0

r3 = Gradientdescent(f,J,-2.0,0.0,0.001,0.5*10**-10)
print(r3)

z3 = Gradientdescent2(f,J,-2.0,0.0,0.001,0.5*10**-10)
print(z3)

x3 = Gradientdescent3(f,J,-2.0,0.0,0.001,0.1,0.5,0.5*10**-10)
print(x3)

#1.5,1.5

r4 = Gradientdescent(f,J,1.5,1.5,0.001,0.5*10**-10)
print(r4)

z4 = Gradientdescent2(f,J,1.5,1.5,0.001,0.5*10**-10)
print(z4)

x4 = Gradientdescent3(f,J,1.5,1.5,0.001,0.1,0.5,0.5*10**-10)
print(x4)

#0,0
r5 = Gradientdescent(f,J,0.1,0.1,0.001,0.5*10**-10)
print(r5)

z5 = Gradientdescent2(f,J,0.1,0.1,0.001,0.5*10**-10)
print(z5)

x5 = Gradientdescent3(f,J,0.1,0.1,0.001,0.1,0.5,0.5*10**-10)
print(x5)