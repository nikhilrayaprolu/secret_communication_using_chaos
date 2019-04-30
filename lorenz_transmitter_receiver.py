import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot
def lorenzreceiver(x, y, z, xin, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*xin - y - xin*z
    z_dot = xin*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty((num_steps + 1,))
ys = np.empty((num_steps + 1,))
zs = np.empty((num_steps + 1,))

xn = np.empty((num_steps + 1,))
yn = np.empty((num_steps + 1,))
zn = np.empty((num_steps + 1,))

# Set initial values
xs[0], ys[0], zs[0] = (40, 40, 40)
xn[0], yn[0], zn[0] = (-40, -40, 40)
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xn[i], yn[i], zn[i], xs[i])
    xn[i + 1] = xn[i] + (x_dot * dt)
    yn[i + 1] = yn[i] + (y_dot * dt)
    zn[i + 1] = zn[i] + (z_dot * dt)

    

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.plot(xn, yn, zn, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()

def Diff(li1, li2): 
    return np.array(li1) - np.array(li2)
def square(list):
    return map(lambda x: x ** 2, list)
x = Diff(xs, xn)
y = Diff(ys, yn)
z = Diff(zs, zn)
xx = square(x)
yy = square(y)
zz = square(z)
final = [sum(n) for n in zip(xx, yy, zz)]
import matplotlib.pyplot as plt
plt.plot(final)
plt.show()
