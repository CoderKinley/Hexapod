import numpy as np
from time import sleep

# Servo class simulation
class Servo:
    def __init__(self, pin, min_pulse, max_pulse):
        self.pin = pin
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.position = 0
    
    def attach(self, pin, min_pulse, max_pulse):
        pass
    
    def write(self, position):
        self.position = position
        print(f"Servo {self.pin} moved to position {position}")
    
    def read(self):
        return self.position

# Define Servo pins
J1Pin = 2
J2Pin = 3
J3Pin = 4

# Servo instances
Joint1 = Servo(J1Pin, 500, 2500)
Joint2 = Servo(J2Pin, 400, 2400)
Joint3 = Servo(J3Pin, 750, 2400)

def cartesian_move(X, Y, Z):
    # OFFSET TO REST POSITION
    Y += 50
    Z -= 80

    # CALCULATE INVERSE KINEMATIC SOLUTION
    J1 = np.degrees(np.arctan(X / Y))
    H = np.sqrt((Y ** 2) + (X ** 2))
    L = np.sqrt((H ** 2) + (Z ** 2))
    J3 = np.degrees(np.arccos(((57 ** 2) + (110 ** 2) - (L ** 2)) / (2 * 57 * 110)))
    B = np.degrees(np.arccos(((L ** 2) + (57 ** 2) - (110 ** 2)) / (2 * L * 57)))
    A = np.degrees(np.arctan(Z / H))  # Note: arctan function here
    J2 = B + A

    update_position(J1, J2, J3)

def update_position(J1, J2, J3):
    # MOVE TO POSITION
    Joint1.write(90 - J1)
    Joint2.write(90 - J2)
    Joint3.write(J3 + 15.4 - 90)

# Loop through commands
for line in lines:
    X, Y, Z, duration = line
    cartesian_move(X, Y, Z)
    sleep(duration / 1000)  # Convert duration to seconds
