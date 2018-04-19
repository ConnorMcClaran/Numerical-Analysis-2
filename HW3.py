#Connor McClaran
#MTH4490
#HW3

import numpy as np



a = np.matrix([[1,0,1],[1 ,1,0 ],[1, 0, 0]])

b = np.matrix([[1,0,-1/3],[0,1,2/3],[-1,1,1]])

c = np.matrix([[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[1,0,0,0]])


Al,Av= np.linalg.eig(a)
Bl,Bv = np.linalg.eig(b)
Cl,Cv = np.linalg.eig(c)

def upperHessenberg(A):
  m,n = A.shape
  for i in range(1,n-1):
      x = A[i:,i-1]
      #print(x)
      w = np.zeros((n-i,1))
      w[0] = np.linalg.norm(x)
      if w[0] == 0:
          continue
      #print(w)
      v = w-x
      #print(v)
      P = (v*v.T)/(v.T*v)
      H = np.eye(n)
      H[i:,i:] = np.eye(n-i)-2*P
      #print(H)
      A = H*A*H
      #print(A)
  return A


a = upperHessenberg(a)


b = upperHessenberg(b)

c = upperHessenberg(c)



def shiftedQR(A,s):
    n = len(A)
    for i in range(0,10):
      I = np.eye(n)
      #s = A[n-1,n-1]
      B = A - s*I
      Q,R = np.linalg.qr(B)
      A = R*Q + s*I
    return A

print(shiftedQR(a,1))
print(Al)


print(shiftedQR(b,2))
print(Bl)

print(shiftedQR(c,1))
print(Cl)

