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




#approximate area under curve y = x^2

def MonteCarloType1(u):
    n = len(u)
    m = 0.0
    for i in range(n):
         m +=(1/float(n))* (u[i])
     
    
    return m 

# x = MonteCarloType1(y31)     
#print(x)  

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
'''
fig,ax = pyplot.subplots()
pyplot.title('Mersenne Prime')
pyplot.scatter(n,m)
pyplot.xlabel('x')
pyplot.ylabel('y')
'''

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
pyplot.title('LCG')
bx.set_xlabel('x')
bx.set_ylabel('y')
bx.set_zlabel('z')

pyplot.show()





fig = pyplot.figure()
cx = fig.add_subplot(111,projection = '3d')
q,w,e = createTriple(v)
cx.scatter(q,w,e,marker='^')
pyplot.title('randu')
cx.set_xlabel('x')
cx.set_ylabel('y')
cx.set_zlabel('z')
pyplot.show()

