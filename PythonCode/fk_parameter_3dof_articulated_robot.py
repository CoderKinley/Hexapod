import numpy as np

# 3DOF articulated robot
# H------------0-------------0-------------------------------------x
# theta1       theta2         theta3

# Author: Kinley Penjor
# Date Created: February  24, 2024

# Joint lengths 
r1 = 4
r2 = 8
r3 = 16

# Joint angles
theta1 = 38.66
theta2 = 40.65
theta3 = -41.41

# angle b/w z-axis along z0
alpha1 = 90
alpha2 = 0
alpha3 = 0

# Declare the Denavit-Hartenberg table. 
t = np.array([[np.deg2rad(theta1), np.deg2rad(alpha1), r1, 0],
                      [np.deg2rad(theta2), np.deg2rad(alpha2), r2, 0],
                      [np.deg2rad(theta3), np.deg2rad(alpha3), r3, 0]
                      ]) 

i = 0
t01 = np.array([[np.cos(t[i,0]), -np.sin(t[i,0]) * np.cos(t[i,1]), np.sin(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.cos(t[i,0])],
                [np.sin(t[i,0]), np.cos(t[i,0]) * np.cos(t[i,1]), -np.cos(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.sin(t[i,0])],
                [0, np.sin(t[i,1]), np.cos(t[i,1]), t[i,3]],
                [0, 0, 0, 1]
                ])  
i = 1 
t12 = np.array([[np.cos(t[i,0]), -np.sin(t[i,0]) * np.cos(t[i,1]), np.sin(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.cos(t[i,0])],
                [np.sin(t[i,0]), np.cos(t[i,0]) * np.cos(t[i,1]), -np.cos(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.sin(t[i,0])],
                [0, np.sin(t[i,1]), np.cos(t[i,1]), t[i,3]],
                [0, 0, 0, 1]
                ])
i = 2
t23 = np.array([[np.cos(t[i,0]), -np.sin(t[i,0]) * np.cos(t[i,1]), np.sin(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.cos(t[i,0])],
                [np.sin(t[i,0]), np.cos(t[i,0]) * np.cos(t[i,1]), -np.cos(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.sin(t[i,0])],
                [0, np.sin(t[i,1]), np.cos(t[i,1]), t[i,3]],
                [0, 0, 0, 1]
                ])  
t02 = t01 @ t12
t02_rounded = np.round(t02, decimals = 3)
t03 = t01 @ t12 @ t23
t01_rounded = np.round(t01, decimals = 3)
t03_rounded = np.round(t03, decimals = 3)
print(t01_rounded)
print()
print(t02_rounded)
print()
print("Homogenous Matrix frame 0 to frame 2")
print(t03_rounded)