import numpy as np
import math as math
def Euler_matrix(phi_1,phi_2,shy):
    z1 = np.array([[np.cos(np.radians(phi_1)) ,np.sin(np.radians(phi_1)),0],
                   [-np.sin(np.radians(phi_1)),np.cos(np.radians(phi_1)),0],
                   [0                         ,0                        ,1]])
    z2 = np.array([[np.cos(np.radians(phi_2)) ,np.sin(np.radians(phi_2)),0],
                   [-np.sin(np.radians(phi_2)),np.cos(np.radians(phi_2)),0],
                   [0                         ,0                        ,1]])
    x2 = np.array([[1                         ,0                        ,0],
                   [0                         ,np.cos(np.radians(shy))  ,np.sin(np.radians(shy))],
                   [0                         ,-np.sin(np.radians(shy)) ,np.cos(np.radians(shy))]])
    R1 = np.matmul(z2,x2)
    R = np.matmul(R1,z1)
    return R
Rotation_matrix = Euler_matrix(20,50,180)
print('Rotation matrix is: \n',Rotation_matrix)

def Euler_angle(Rot):
      if Rot[2][2] ==1:
            phi_11 = np.degrees((math.atan(Rot[0][1]/Rot[0][0]))/2)
            phi_12 = phi_11
            shy1 = np.degrees(math.acos(Rot[2][2]))
      else:
            shy1 = np.degrees(math.acos(Rot[2][2]))
            #phi_11 = math.atan(((Rot[2][0])/np.sin(np.radians(shy1)))/((Rot[2][1])/np.sin(np.radians(shy1))))
            phi_11 = np.degrees(math.atan(((Rot[2][0])/np.sin((shy1)))/(-(Rot[2][1])/np.sin((shy1)))))
            #phi_12 = math.atan(((Rot[0][2])/np.sin(np.radians(shy1)))/((Rot[1][2])/np.sin(np.radians(shy1)))) 
            phi_12 = np.degrees(math.atan(((Rot[0][2])/np.sin((shy1)))/((Rot[1][2])/np.sin((shy1))))) 
      
      return phi_11,phi_12,shy1

Euler_angles = Euler_angle(Rotation_matrix)
print('Eurler angles are Phi_1,Phi_2,Shy: \n',Euler_angles)
   