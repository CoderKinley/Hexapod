import numpy as np
import keyboard
import time
import matplotlib.pyplot as plt

class Robot2DOF:
    def __init__(self, x, y, l1, l2):
        self.x = x
        self.y = y
        self.l1 = l1
        self.l2 = l2
        self.terminating_flag = False
        self.x_positions = []
        self.y_positions = []

    # this will calculate the forward kinematics in 2DOF planar robot
    def convert2rad(self, val):
        radian = np.deg2rad(val)
        return radian

    def inverse_kinematics(self, x, y):
        l3 = np.sqrt((x ** 2) + (y ** 2))
        a1 = np.arctan2(y, x)
        a2 = np.arccos(((self.l1 ** 2) + (l3 ** 2) - (self.l2 ** 2)) / (2 * self.l1 * l3))
        a3 = np.arccos(((self.l1 ** 2) + (self.l2 ** 2) - (l3 ** 2)) / (2 * self.l1 * self.l2))
        alpha1 = np.degrees(a1)
        alpha2 = np.degrees(a2)
        alpha3 = np.degrees(a3)

        calculated_theta1 = alpha1 + alpha2
        calculated_theta2 = alpha3 - 180

        x1 = self.l1 * np.cos(self.convert2rad(calculated_theta1))
        y1 = self.l1 * np.sin(self.convert2rad(calculated_theta1))
        
        print("x1: ", x1, " y1: ", y1)

        return calculated_theta1, calculated_theta2

    def simulate(self):
        keyboard.hook(self.key_event_listener)

        # Define circle parameters
        center_x = 15
        center_y = 10
        radius = 5
        num_points = 50
        angle_step = 360 / num_points

        for i in range(num_points):
            angle_degrees = i * angle_step
            angle_radians = np.radians(angle_degrees)
            target_x = center_x + radius * np.cos(angle_radians)
            target_y = center_y + radius * np.sin(angle_radians)

            theta1, theta2 = self.inverse_kinematics(target_x, target_y)
            print("Theta1: {:.2f} degrees, Theta2: {:.2f} degrees".format(theta1, theta2))

            # using the fwk to calculate the position of the joing of femur and tibia
            self.x_positions.append(target_x)
            self.y_positions.append(target_y)

            # Uncomment this to move the robot (simulated movement)
            # time.sleep(0.1)

        # Plot the movement
        plt.plot(self.x_positions, self.y_positions, 'b-')
        plt.plot(self.x_positions, self.y_positions, 'ro')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('End Effector Movement')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()

    def key_event_listener(self, e):
        if e.event_type == keyboard.KEY_DOWN:
            if e.name.lower() == "esc":
                self.terminating_flag = True
                print("Terminating program...")

def main():
    x = 20
    y = 0
    l1 = 8
    l2 = 16
    robot = Robot2DOF(x, y, l1, l2)
    robot.simulate()

if __name__ == "__main__":
    main()
