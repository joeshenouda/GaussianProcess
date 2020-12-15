import numpy as np

m=4
T=5

E = np.zeros((m*T-m, m*T))
for i in range(m*T-m):
    if (i+1) % T != 0:
        E[i, i//T+i] = 1
    else:
        E[i, i+(i+1)//T] = 1
print(E)