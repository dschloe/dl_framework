if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dezero import Variable
# import dezero's simple_core explicitly
import dezero
if not dezero.is_simple_core:
    from dezero.core_simple import Variable
    from dezero.core_simple import setup_variable
    setup_variable()


def rosenbrock(x0, x1):
    y = 100 * (x1 - x0 ** 2) ** 2 + (x0 - 1) ** 2
    return y


x0 = Variable(np.array(0.0))
x1 = Variable(np.array(2.0))
lr = 0.001
iters = 1000

for i in range(iters):
    print(x0, x1)

    y = rosenbrock(x0, x1)

    x0.cleargrad()
    x1.cleargrad()
    y.backward()

    x0.data -= lr * x0.grad
    x1.data -= lr * x1.grad

lr=0.001 #학습률
iters=50000 #epoch
result1 = []
result2 = []
for i in range(iters):
    print(x0.data,x1.data)
    y=rosenbrock(x0,x1)
    x0.cleargrad()
    x1.cleargrad()
    y.backward()
    x0.data=x0.data-lr*x0.grad
    x1.data=x1.data-lr*x1.grad
    result1.append(x0.data)
    result2.append(x1.data)

print(result1)
print(result2)
print(result1[-2:-1])
print(result2[-2:-1])

# =============================================================================
# Visualize for computational graph
# =============================================================================

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm

x0 = np.arange(-2, 2, 0.15)
x1 = np.arange(-1, 3, 0.15)
x0, x1 = np.meshgrid(x0, x1)
z = rosenbrock(x0,x1)

figRos = plt.figure(figsize=(12, 7))
axRos = figRos.gca(projection='3d')
surf = axRos.plot_surface(x0, x1, z, cmap=cm.get_cmap(),linewidth=0, antialiased=False)
axRos.set_zlim(0, 2000)
figRos.colorbar(surf, shrink=0.5, aspect=10)
# plt.show()

plt.figure(figsize=(12, 7))
plt.contour(x0,x1,z,700)
for i,j in zip(result1,result2):
    plt.plot(i,j,marker='o',markersize=5, color ='cyan')
    plt.plot(1.0,1.0,marker='x',markersize=15, color ='r')

plt.show()