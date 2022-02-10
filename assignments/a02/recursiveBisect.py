#!/user/bin/python3
from telnetlib import EL
from tracemalloc import stop
import numpy as np


def bisecRecursive(xhigh,xlow):
    xhalf=(xhigh+xlow)/2
    x_low=0
    x_hi=0
    if np.sign(np.exp(xhalf)-4) == np.sign(np.exp(xlow)-4):
        x_low = xhalf
        x_hi = xhigh
    else:
        x_hi = xhalf
        x_low = xlow
    return np.array([x_low,x_hi,xhalf])

x_hi=6
x_low=-2

stop_spot = 10**(-6)
ind = 1
while (x_hi-x_low) >= stop_spot:
    x_hi = bisecRecursive(x_hi,x_low)[1]
    x_low = bisecRecursive(x_hi,x_low)[0]
    xhalf = bisecRecursive(x_hi,x_low)[2]
    print('Iteration ',ind,' : ', x_hi,x_low,np.exp(xhalf)-4)
    ind = ind+1

print('Approximated solution of f(x)=0 : x=', xhalf)
