import numpy as np

def inverse_kinematics():
    x = 20
    y = 16
    z = 5
    a1 = 4
    a2 = 8
    a3 = 16

    theta1 = np.degrees(np.arctan(y/x))
    a4 = np.sqrt((pow((x-a1),2))+(pow(a3,2)))
    phi3 = np.arccos(((pow(a2,2))+(pow(a4,2))-(pow(a3,2)))/(2*a2*a4))
    phi2 = np.arcsin(z/a4)
    phi3 = np.degrees(phi3)
    phi2 = np.degrees(phi2)
    theta2 = phi2 + phi3
    val = ((pow(a2,2))+(pow(a3,2))-(pow(a4,2)))/(2*a2*a3)
    phi1 = np.degrees(np.arccos(val))
    theta3 =  phi1 - 180
    print(theta1, theta2, theta3)

inverse_kinematics()