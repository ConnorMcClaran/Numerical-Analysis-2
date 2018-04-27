import numpy as np 
import matplotlib as pltlib



#Connor McClaran Project 2
#mth4490


# analyze and create random number generators 



import random 




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
    

y31 = np.zeros(10)
y31 = mod31(3,10)

print(y31)


 
