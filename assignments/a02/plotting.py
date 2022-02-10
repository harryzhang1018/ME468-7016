#!/user/bin/python3

import matplotlib.pyplot as plt
import numpy as np

n = np.array([2**9,2**10,2**11,2**12,2**13])
avg_time_loop = np.array([463.68, 1971.16, 8600.105, 34595.5, 145581.8])
avg_time_np = np.array([0.2185,1.11,4.8487,17.88,69.13])

plt.semilogx(n,avg_time_loop,'-*',label="loop")
plt.semilogx(n,avg_time_np,'-o',label="numpy")
plt.xlabel('n in log scale (dimension of Matrix)')
plt.ylabel('Running time (ms)')
plt.title('Windows11-GeForceRXT2060-16GB')
plt.legend()
plt.show()
