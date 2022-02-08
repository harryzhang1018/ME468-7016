#!/user/bin/python3

from turtle import st
import numpy as np
import timeit
import sys
from setuptools import setup

n = int(sys.argv[-1])

A = np.random.uniform (-1,1,(n,n))
b = np.ones([n,1])


def loopCal(A,b):
    c = np.zeros([n,1])
    for i in range(n):
        for j in range(n):
            c[i] += A[i,j]*b[j,0]
    return c[-1]

def npCal(A,b):
    c = np.zeros([n,1])
    c = np.dot(A,b)
    return c[-1]

time1 = np.zeros(20)
time2 = np.zeros(20)


for i in range(20):
    mysetup='''
from __main__ import loopCal
from __main__ import A    
from __main__ import b'''
    mycode='''
c1=loopCal(A,b)
'''
    #c1=loopCal(A,b)
    time1[i] =timeit.timeit(setup=mysetup, stmt=mycode,number=1) *1000 #in ms scale
c1=loopCal(A,b)
avg_time1 = sum(time1)/20
std1 = np.std(time1)


for i in range(20):
    mysetup2='''
from __main__ import npCal
from __main__ import A    
from __main__ import b'''
    mycode2='''
c2=npCal(A,b)
'''
    time2[i] =timeit.timeit(setup=mysetup2, stmt=mycode2,number=1) *1000 #in ms scale
c2=npCal(A,b)
avg_time2 = sum(time2)/20
std2 = np.std(time2)
print(c1)
print(avg_time1)
print(std1)
print(c2)
print(avg_time2)
print(std2)









