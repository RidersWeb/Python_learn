from copy import copy
import numpy as np

a = np.array(range(9), int)

b = copy(a)
b[5] = 8
b[8] = 5

print(a)
print(b)

c = np.concatenate((a,b))
print(c)

d  = c.reshape((6,3))
print(d)