if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np

x = np.array([[1,2,3], [4,5,6]])
y = np.reshape(x, (6, ))
print(y)
# [1 2 3 4 5 6]

from dezero import Variable
import dezero.functions as F

x = Variable(np.array([[1,2,3], [4,5,6]]))
y = F.reshape(x, (6,))
y.backward(retain_grad=True)
print(x.grad)

x = np.random.rand(1,2,3)
y = x.reshape((2, 3)) # 튜플로 받기 
y = x.reshape(([2,3])) # 리스트로 받기
y = x.reshape(2,3) # 인수를 그대로(풀어서) 받기
print(y)

x = Variable(np.random.randn(1, 2, 3))
y = x.reshape((2, 3))
print(y)
y = x.reshape(2,3)
print(y)

x = np.array([[1,2,3], [4,5,6]])
y = np.transpose(x)
print(y)

x = Variable(np.array([[1,2,3], [4,5,6]]))
y = F.transpose(x)
y.backward()
print(x.grad)

x = Variable(np.random.rand(2,3))
print(x)
y = x.transpose()
print(y)
y = x.T
print(y)

A, B, C, D = 1, 2, 3, 4
x = np.random.rand(A, B, C, D)
print(x)
y = x.transpose(1, 0, 3, 2)
print(y)