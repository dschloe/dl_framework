# Add import path for the dezero directory.
if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from dezero import Variable
from dezero.utils import get_dot_graph, _dot_var, _dot_func

'''
# page 216 그래프
x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))
y = x0 + x1

x0.name = 'x0'
x1.name = 'x1'
y.name = 'y'

txt = get_dot_graph(y, verbose=True)
print(txt)

with open('sample.dot', 'w') as o:
    o.write(txt)
'''

'''
page 217

x = Variable(np.random.randn(2, 3))
x.name = 'x'
print(_dot_var(x))
print(_dot_var(x, verbose=True))
2994949629120 [label="x", color=orange, style=filled]
2994949629120 [label="x: (2, 3) float64", color=orange, style=filled]
'''

'''
page 218

x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))
y = x0 + x1
txt = _dot_func(y.creator)
print(txt)
2588175672416 [label="Add", color=lightblue, style=filled, shape=box]
2588175672512 -> 2588175672416
2588175671936 -> 2588175672416
2588175672416 -> 2588214343568
'''



