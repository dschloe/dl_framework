class Variable:
    def __init__(self, data):
        self.data = data

import numpy as np
data = np.array(2.0)
x = Variable(data)
print(x.data)