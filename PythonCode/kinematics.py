import numpy as np
import keyboard

class Robot2DOF:
    def __init__(self, x, y, l1, l2):
        self.x = x
        self.y = y
        self.l1 = l1
        self.l2 = l2
        self.terminating_flag = False
    
    # this will calculate the forward kinematics in 2DOF planer robot
    def convert2rad(self, val):
        radian = np.deg2rad(val)
        return radian

    def inverse_kinematics(self):    
        l3 = np.sqrt((pow(self.x,2))+(pow(self.y,2)))
        a1 = np.arctan(self.y/self.x)
        a2 = np.arccos(((pow(self.l1,2))+(pow(l3,2))-(pow(self.l2,2)))/(2*self.l1*l3))
        a3 = np.arccos(((pow(self.l1,2))+(pow(self.l2,2))-(pow(l3,2)))/(2*self.l1*self.l2))
        alpha1 = np.degrees(a1)
        alpha2 = np.degrees(a2)
        alpha3 = np.degrees(a3)
        
        calculated_theta1 = alpha1 + alpha2
        calculated_theta2 = alpha3 - 180

        x1, y1 = self.forward_kinematics(self.l1, self.l2, calculated_theta1, calculated_theta2)

        return calculated_theta1, calculated_theta2, x1, y1

    def forward_kinematics(self, l1, l2, theta1, theta2):
        x1 = l1 * np.cos(self.convert2rad(theta1))
        y1 = l1 * np.sin(self.convert2rad(theta1))
        
        # this will be used to calculate the end effector point
        x2 = x1 + (l2 * np.cos(self.convert2rad(theta1) + self.convert2rad(theta2))) 
        y2 = y1 + (l2 * np.sin(self.convert2rad(theta1) + self.convert2rad(theta2)))

        return(x1, y1)
    
    def key_event_listener(self,e):
        if (e.event_type == keyboard.KEY_DOWN):
            self.terminating_flag = True
            print("terminating program...")

    def simulate(self):
        keyboard.hook(self.key_event_listener)
        while not self.terminating_flag:
            alpha, beta, x1, y1 = self.inverse_kinematics()
            print("alpha -->", alpha, "beta -->", beta)
            print("x1 -->", x1, "y1 -->", y1)
    
def main():
    x = 20
    y = 0
    l1 = 8 
    l2 = 16
    robot = Robot2DOF(x,y,l1,l2)
    robot.simulate()

if __name__=="__main__":
    main()