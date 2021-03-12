if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import dezero.functions as F
from dezero import Variable

# (스칼라 방식)
x = Variable(np.array(1.0))
y = F.sin(x)
print(y)

# 텐서 방식
x = Variable(np.array([[1,2,3], [4,5,6]]))
y = F.sin(x)
print(y)

# sin 함수 각 x의 원소 각각에 적용하여 입력과 출력 텐서의 형상은 영향을 받지 않음
x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
c = Variable(np.array([[10, 20, 30], [40, 50, 60]]))
y = x + c 
print(y)

y.backward(retain_grad=True)
print(y.grad)
print(x.grad)
print(c.grad)
print(t.grad)

