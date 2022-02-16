import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode

m = 1000
ks = 50000
cs = 4000
los = 0.4
g = 10

x_ini = m*g/(4*ks)
x_eq = los - x_ini
v_ini = 0

def fun(t, z):
    """
    Right hand side of the differential equations
      dx/dt = v
      dv/dt = -cs / m - ks/m * x
    """
    x, y = z
    f = [y,-cs / m*y - ks/m * x]
    return f

solver = ode(fun)
solver.set_integrator('dop853')

t0 = 0.0
z0 = [x_ini, v_ini]
solver.set_initial_value(z0, t0)

t1 = 5
N = 100
t = np.linspace(t0, t1, N)
sol = np.empty((N, 2))
sol[0] = z0

k = 1
while solver.successful() and solver.t < t1:
    solver.integrate(t[k])
    sol[k] = solver.y
    k += 1
sol[:,0]=sol[:,0]+x_eq

plt.figure()
plt.plot(t, sol[:,0])
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.title('Position vs Time')
plt.show()
plt.figure()
plt.plot(t, sol[:,1], label='v')
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.title('Velocity vs Time')
plt.show()