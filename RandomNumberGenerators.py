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

def mod31(seed,n):
    x = [seed]
    u = []
    for i in range(n):
        x.append((13*x[i])%31)
        u.append(x[i]/31.0)
    return u	
    

y31 = np.zeros(30)
y31 = mod31(3,30)
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


n = np.arange(30)

                                                                      
fig,dx = pyplot.subplots()
pyplot.title('simple psuedo random scatter plot')
pyplot.scatter(n,y31)

pyplot.xlabel('x')
pyplot.ylabel('y')

dx.legend()

pyplot.show()
