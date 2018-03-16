import numpy as np
from matplotlib import pyplot
import pandas
import scipy

#Problem 1

def rk4_step(f,t,w,h):
    s1 = f(t,w)
    s2 = f(t+h/2,w+(h/2)*s1)
    s3 = f(t+h/2,w+(h/2)*s2)
    s4 = f(t+h,w+h*s3)
    return w + (h/6)*(s1+2*s2+2*s3+s4)

#y1
def qf(t,q):
    return np.array(q[1],np.exp(t) + q[0]*np.cos(t) - (t+1)*q[1])
#y2
def zf(t,z):
    return np.array(z[1],np.exp(t) + z[0]*np.cos(t) - (t+1)*z[1])

I = [1,3]
n = 200

q = np.zeros((n+1,2))

z = np.zeros((n+1,2))

w = np.zeros((n+1))

h = (I[1]-I[0])/n

t = [I[0]+i*h for i in range(n+1)]

q[0,:] = [1,0]
z[0,:] = [0,1]

for i in range(n):
    q[i+1,:] = rk4_step(qf,t[i],q[i,:],h)
    z[i+1,:] = rk4_step(zf,t[i],z[i,:],h)

for i in range(n+1):
    w[i] = q[i,0]+(I[1]-q[n,0])*z[i,0]/z[n,0]


fig,ax = pyplot.subplots()
pyplot.title('Problem 1 Solution')
ax.plot(t,w)
ax.set_xlabel('t')
ax.set_ylabel('Approximate Solution')
pyplot.show()

'''

t = [0,10]
x = [0,22]
h = 0.02
k = 0.0001
D = 1

sigma = (D*k)/(h**2)
M = 1100
A = np.zeros((M,M))
np.fill_diagonal(A,(1-(2*sigma)))

'''