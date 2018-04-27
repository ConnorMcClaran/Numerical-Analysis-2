import numpy as np 
import matplotlib.pyplot as pyplot
import random 


#Connor McClaran Project 2
#mth4490


# analyze and create random number generators 


random.seed(a = None)


x = random.getstate()

#print(x)

#psuedo random number (mod 31)

def mod31(seed,A,b,m,n):
    x = [seed]
    u = []
    m = float(m)
    for i in range(n):
        x.append((A*x[i])%m)
        u.append(x[i]/m)
    return u	
    

y31 = np.zeros(30)
y31 = mod31(3,13,0,31.0,30)
print(y31)



# linear Congruential generator (LCG)

#x[i] =( Ax[i] + b ) mod m 
# u = x[i] / m 

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

m = mod31(3,7**5,0,2**31 - 1,10000)
n = np.arange(10000)
fig,ax = pyplot.subplots()
pyplot.title('Mersenne Prime')
pyplot.scatter(n,m)
pyplot.xlabel('x')
pyplot.ylabel('y')


pyplot.show() 
