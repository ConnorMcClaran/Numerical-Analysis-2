from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import matplotlib.pyplot as pyplot
import random 


#Connor McClaran Project 2
#mth4490


# analyze and create random number generators 

#random seed based on system time
random.seed(a = None)


x = random.getstate()

#print(x)


# linear Congruential generator (LCG)

#x[i] =( Ax[i] + b ) mod m 
# u = x[i] / m 



def LCG(seed,A,b,m,n):
    x = [seed]
    u = []
    m = float(m)
    for i in range(n):
        x.append((A*x[i])%m)
        u.append(x[i]/m)
    return u	
    

y31 = np.zeros(30)
y31 = LCG(3,13,0,31.0,30)

     


## plot - simple psuedo random generator (mod31)##
n = np.arange(30)                                                                      
fig,dx = pyplot.subplots()
pyplot.title('simple psuedo random scatter plot')
pyplot.scatter(n,y31)
pyplot.xlabel('x')
pyplot.ylabel('y')
dx.legend()
#################################################
pyplot.show()

#Mersenne Prime

m = LCG(3,7**5,0,2**31 - 1,10000)
n = np.arange(10000)

fig,ax = pyplot.subplots()
pyplot.title('Mersenne Prime')
pyplot.scatter(n,m)
pyplot.xlabel('x')
pyplot.ylabel('y')


pyplot.show()

#create 3D scatter Plot
#triples

#Randu generator
v = LCG(1,65539,0,2**31,10000)

def createTriple(m):
    x =[]
    y = []
    z = []
    n = len(m)
    for i in range(n-2):
        x.append( m[i])
        y.append( m[i+1] )
        z.append( m[i+2]) 
    return x,y,z



fig = pyplot.figure()
bx = fig.add_subplot(111,projection ='3d')
x,y,z = createTriple(m)
bx.scatter(x,y,z,color = 'green')
pyplot.title('LCG,minimal standard')
bx.set_xlabel('x')
bx.set_ylabel('y')
bx.set_zlabel('z')

pyplot.show()





fig = pyplot.figure()
cx = fig.add_subplot(111,projection = '3d')
q,w,e = createTriple(v)
cx.scatter(q,w,e,marker='^')
pyplot.title('Randu')
cx.set_xlabel('x')
cx.set_ylabel('y')
cx.set_zlabel('z')
pyplot.show()



def MC1(x):
    n = len(x)
    y = []
    s = 0.0
    for i in range(n):
        y.append((x[i])**2)
    return np.absolute(np.mean(y)-(1/3.0))
z1 = []
z2 = []
z3 = []
z4 = []
z5 = []
z6 = []
z7 = []
z8 = []
z9 = []
z10 = []
z11 = []
z12 = []


for i in range(30):

    x1 = LCG(5,7*5,0,2**31 -1,10**2) 
    n1 = np.random.rand(10**2)
    
    x2 = LCG(5,65539,0,2**31,10**2)
    n2 = np.random.rand(10**4)

    
    x3 = LCG(5,7*5,0,2**31 -1,10**4)
    n3 = np.random.rand(10**6)
    
    x4 = LCG(5,65539,0,2**31,10**4)

    x5 = LCG(5,7*5,0,2**31 -1,10**6)
    x6 = LCG(5,65539,0,2**31,10**6) 
    z1.append(MC1(x1))
    z2.append(MC1(x2))
    z3.append(MC1(x3))
    z4.append(MC1(x4))
    z5.append(MC1(x5))  
    z6.append(MC1(x6))
    z7.append(MC1(n1))
    z8.append(MC1(n2))
    z9.append(MC1(n3))
  

                   


tens = [10**2,10**4,10**6]
m = [np.mean(z1),np.mean(z3),np.mean(z5)]#minmal standard
m2 = [np.mean(z2),np.mean(z4),np.mean(z6)] # Randu
m3 = [np.mean(z7),np.mean(z8),np.mean(z9)] # np.random.rand

fig,ex = pyplot.subplots()
pyplot.title('Type 1 Error')
ex.set_yscale('log')
ex.set_xscale('log')
pyplot.ylabel('Error')
pyplot.xlabel('Number of points N')
ex.plot(tens,m,marker = 'o',linestyle = '--',label = 'MinStandard')
ex.plot(tens,m2,marker = '^',linestyle = '--',label = 'Randu')
ex.plot(tens,m3,marker = 'p',linestyle = '--',label = 'np.rand')

ex.legend()
pyplot.show()










