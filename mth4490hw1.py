#Connor McClaran
#MTH4490 HW1

#y'(t) = 4t - 2y(t) d'Alembert's equation

def f(t,w):
	return 4*t - 2*w
	
def Euler(f,a,b,y0,n):
        h = (b-a)/float(n)
        x = a
        y = y0
        for i in range(n):
                y += h*f(x,y)
                x += h
        return y

#Test at y0 = 0

print(Euler(f,0,1,0,4))




        
