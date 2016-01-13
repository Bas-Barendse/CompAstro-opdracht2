import numpy as np
import matplotlib.pyplot as plt

def hoi(x):
    return x*2
    
def exponent(x):
    return np.exp(x)

def exp2(x, b):
    return np.exp(x)+b

def simpson(func, a,Hn):
    """prefoms simpsun rule at specific point"""
    
    b = a + Hn
    c = (a + b)/2
    result = Hn/6.*(func(a)+4*func(c)+func(b))
        
    return result
    
def adv_simpson(func, a, Hn, N):
    """prefoms simpsun rule at specific point"""
    
    b = a + Hn
    c = (a + b)/2
    result = Hn/6.*(func(a)+4*func(c)+func(b))
        
    return result


def intergrate(func, a, b, N, *args):
    """in which func is the name of the function (object function), a, b the left and 
    right boundries (floats) N (int) the number of intervals which it intergates over
    Function returns the value of the intergal over func"""
    
    
    Hn = (b-a)/N        #step size on intergation axis

    # make list of points on intergation axis
    arr = np.arange(0,N+1,1)
    arr = arr*Hn+a
    
    # make list of 1/3., 2/3. alternating as long as the list of arr
    
    
    result = func(arr, *args)
    result[0] *= 1/3.
    result[1::2] *= 4/3.
    result[2::2] *= 2/3.
    result[-1] *= 1/3.
    result *= Hn
    
    print result.sum()
    
    
    # calculate intergral
##     intergrad = adv_simpson(func, arr[0:-1], Hn, N)
##     print intergrad.sum()
    
    
    
if __name__ == "__main__":
    #intergrate(hoi, 0.,5.,100)
    intergrate(exponent, 0., 1., 10000)
    #intergrate(exp2, 0., 1., 10000, 1.)
    
    