if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import math
from dezero import Function
from dezero import Variable
from dezero.utils import plot_dot_graph

class Sin(Function):
    def forward(self, x):
        """
        Forward of sin(x)
        
        returns: float
        """
        y = np.sin(x)
        return y
    
    def backward(self, gy):
        """
        differentiation of sin(x) is equal to cos(x)
        gx : backward of sin(x), forward of sin(x) * derivation of sin(x)
        
        returns: float
        """
        x = self.inputs[0].data
        gx = gy * np.cos(x)
        return y
        
def sin(x):
    return Sin()(x)

'''when x= 𝝿/4, differentiate y=sin(x).'''
x = Variable(np.array(np.pi/4))
y = sin(x)
y.backward()

print(y.data)
print(x.grad.data) # x의 미분 값

import math

def my_sin(x, threshold=0.0001):
    
    """ calculate talor series of sin(x) to 100000th derivation, unless (i)th derivation of sin(x) is smaller than threshold(0.0001)
    Args:
    threshold : absolut difference f(x) and f(x+𝛥)
    
    parameters :  
    c : (i)th of function [(-1)ˆi/(2*i+1)!]
    t : (i)th derivation of sin(x), multiply (i)th of function c and (i)th of xˆ(2*i+1)
    y : tayor series value of sin(x).
    
    """
    y = 0
    for i in range(100000):
        c = (-1)**i / math.factorial(2*i+1)
        t = c * x **(2*i+1)
        y = y+t
        if abs(t.data) < threshold:
            break
    return y

x = Variable(np.array(np.pi/4))
y = my_sin(x)
y.backward()

print(y.data) #my_sin 함수에 의한 값
print(x.grad.data) # x의 미분 값

x.name = 'x'
y.name = 'y'
plot_dot_graph(y, verbose=False, to_file='my_sin.png')