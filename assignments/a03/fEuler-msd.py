import numpy as np
import matplotlib.pyplot as plt

step_size=10**(-4)
duration = 5
t_range = np.arange(0,duration+step_size,step_size)

m = 1000
ks = 50000
cs = 4000
los = 0.4
g = 10

x_ini = m*g/(4*ks)
x_eq = los - x_ini
v_ini = 0

def xdot(x,v):
    x_dotdot = -(4*cs/m)*v - (4*ks/m) * x
    return np.array(([v],[x_dotdot]))

x = np.zeros((2,t_range.size))
x[0,0] = x_ini
x[1,0] = v_ini

for i in np.arange(1,t_range.size):
    x_dot = xdot(x[0,i-1],x[1,i-1])
    x[0,i] = x[0, i-1] + step_size * x_dot[0,0]
    x[1,i] = x[1, i-1] + step_size * x_dot[1,0]

position = np.zeros(t_range.size)
position = x[0,:] + x_eq

plt.figure()
plt.plot(t_range,position)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position of Sprung Mass')
plt.show()

pos_solution = np.exp(-8*t_range) * ( 1/20 * np.cos(2*np.sqrt(34)* t_range)+ np.sin(2*np.sqrt(34)* t_range) / (5*np.sqrt(34)))+0.35
vel_solution = -5 * np.exp(-8 * t_range) * np.sin(2*np.sqrt(34)*t_range) / (np.sqrt(34))

e_pos4 = np.max(np.abs(pos_solution-position))
e_vel4 = np.max(np.abs(x[1,:]-vel_solution))
print('largest position error (h=1e-4) is : ',e_pos4)
print('largest velocity error (h=1e-4) is : ',e_vel4)

def calError(h):
    tspan = np.arange(0,duration+h,h)
    x_vec = np.zeros((2,tspan.size))
    x_vec[0,0] = x_ini  
    x_vec[1,0] = v_ini
    for i in np.arange(1,tspan.size):
        x_vec_dot = xdot(x_vec[0,i-1],x_vec[1,i-1])
        x_vec[0,i] = x_vec[0, i-1] + h * x_vec_dot[0,0]
        x_vec[1,i] = x_vec[1, i-1] + h * x_vec_dot[1,0]
    positionOfMass = np.zeros(tspan.size)
    positionOfMass = x_vec[0,:] + x_eq
    pos_sol = np.exp(-8*tspan) * ( 1/20 * np.cos(2*np.sqrt(34)* tspan)+ np.sin(2*np.sqrt(34)* tspan) / (5*np.sqrt(34)))+0.35
    vel_sol = -5 * np.exp(-8 * tspan) * np.sin(2*np.sqrt(34)*tspan) / (np.sqrt(34))
    err_pos = np.max(np.abs(pos_sol-positionOfMass))
    err_vel = np.max(np.abs(x_vec[1,:]-vel_sol))
    return np.array(([err_pos],[err_vel]))

StepSizeList = np.array([10**(-1),10**(-2),10**(-3),10**(-4),10**(-5)])
e_pos = np.zeros(5)
e_vel = np.zeros(5)

for i in np.arange(0,StepSizeList.size):
    e_pos[i] = calError(StepSizeList[i])[0]
    e_vel[i] = calError(StepSizeList[i])[1]

plt.figure()
plt.loglog(StepSizeList,e_pos,label='Position Error')
plt.loglog(StepSizeList, e_vel, label='Velocity Error')
plt.legend()
plt.xlabel('Time Step (s)')
plt.ylabel('Error (m or m/s)')
plt.title('Error vs Time Step')
plt.show()

