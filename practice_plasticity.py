import numpy as np 
import math as math
x = np.cos(np.radians(45))
#print(x)

z1 = [[np.cos(np.radians(0)),np.sin(np.radians(0)),0],
      [-np.sin(np.radians(0)),np.cos(np.radians(0)),0],
      [0                   ,0                     ,1]]

print(z1[2][2])
#shy1 = math.acos(z1(2,2))
#print(shy1)

A = np.array([[1,0,0],
              [0,1,0]])
g = A.transpose(1,0)
print(g)

a = 1:1:10
print(a)