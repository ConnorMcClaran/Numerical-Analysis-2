import numpy as np
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

#Connor McClaran
#Optimizers




#f(x,y = (1-x**2) + 100*(y-x**2)**2


def f(x,y):
    return (1 - x**2) + 100*(((y - x**2))**2)
def T(x,y):
    return  np.sin((0.5*x**2) - (1/4.0)*y**2 +3)*np.cos(2*x + 1 - np.exp(y))
y = np.linspace(0.0,2.0,num = 100)
x = np.linspace(-2.0,2.0,num = 100)
t = []
z = []
for i in range(100):
    z.append(f(x[i],y[i]))
    t.append(T(x,y))


fig  = pyplot.figure()

banana = fig.add_subplot(111,projection = '3d')
pyplot.title('f(x,y) on x[-2.0,2.0] y[0,2.0]')
banana.plot(x,y,z,label = 'banana')
#banana.plot(x,t,label = 'surface')
banana.set_xlabel('x')
pyplot.legend()
banana.set_ylabel('y')
banana.set_zlabel('f(x,y)')
pyplot.show()



#Minimize with Golden Section Search

def gss(a,b,f,tol):
    g = (np.sqrt(5.0-1.0)/2.0)
    k = np.int(np.ceil(np.log(1.0*tol/b-a))/np.log(g))
    x1 = a + (1.0 -g)*(b-a)
    x2 = a +g*(b-a)
    f1 = f(x1,y1)
    f2 = f(x2,y2)
