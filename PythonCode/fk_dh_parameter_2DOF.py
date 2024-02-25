import numpy as np

# 2DOF planer robot
# Author: Kinley Penjor
# Date Created: February  24, 2024

a1 = 8
a2 = 16
theta1 = 10
theta2 = 25
alpha1 = 0
alpha2 = 0

# Declare the Denavit-Hartenberg table. 
# It will have four columns, to represent:
# theta, alpha, r, and d
# We have the convert angles to radians.
t = np.array([[np.deg2rad(theta1), np.deg2rad(alpha1), a1, 0],
                      [np.deg2rad(theta2), np.deg2rad(alpha2), a2, 0]]) 

# homogenous transformation from frame 0 to frame 1
i = 0
t01= np.array([[np.cos(t[i,0]), -np.sin(t[i,0]) * np.cos(t[i,1]), np.sin(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.cos(t[i,0])],
                      [np.sin(t[i,0]), np.cos(t[i,0]) * np.cos(t[i,1]), -np.cos(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.sin(t[i,0])],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])  
i = 1 
t12 = np.array([[np.cos(t[i,0]), -np.sin(t[i,0]) * np.cos(t[i,1]), np.sin(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.cos(t[i,0])],
                      [np.sin(t[i,0]), np.cos(t[i,0]) * np.cos(t[i,1]), -np.cos(t[i,0]) * np.sin(t[i,1]), t[i,2] * np.sin(t[i,0])],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])  

t03 = t01 @ t12
t03_rounded = np.round(t03,decimals = 3)

print(np.deg2rad(0))
print()
print(t01)
print()
print(t12)
print()
print("Homogenous Matrix frame 0 to frame 2")
print(t03_rounded)