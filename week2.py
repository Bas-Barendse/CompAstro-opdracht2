import numpy as np
import matplotlib.pyplot as plt

def hoi(x):
    return x*2

def simpson(func, a,Hn):
    """prefoms simpsun rule at specific point"""
    b = a + Hn
    c = (a + b)/2
    result = Hn/6.*(func(a)+4*func(c)+func(b))
        
    return result

def intergrate(func, a, b, N):
    """in which func is the name of the function (object function), a, b the left and 
    right boundries (floats) N (int) the number of intervals which it intergates over
    Function returns the value of the intergal over func"""
    
    
    Hn = (b-a)/N
    print Hn
    arr = np.arange(0,N+1,1)
    arr = arr*Hn+a
    print arr
    Intergrad = simpson(func, arr[0:-1], Hn)
    
    print Intergrad.sum()
    
    
    
if __name__ == "__main__":
    intergrate(hoi, 0.,5.,100)
    
    
    