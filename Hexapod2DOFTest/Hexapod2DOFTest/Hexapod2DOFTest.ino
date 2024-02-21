#include <Servo.h>

class Robot2DOF {
  private:
    float x, y, l1, l2;
    Servo servo1;
    Servo servo2;

    float toRadians(float degrees) {
      return degrees * PI / 180.0;
    }

    float toDegrees(float radians) {
      return radians * 180.0 / PI;
    }

    void inverseKinematics(float x, float y, float &theta1, float &theta2, float &x1, float &y1) {
      float l3 = sqrt(sq(x) + sq(y));
      float a1 = atan2(y, x);
      float a2 = acos((sq(l1) + sq(l3) - sq(l2)) / (2 * l1 * l3));
      float a3 = acos((sq(l1) + sq(l2) - sq(l3)) / (2 * l1 * l2));
      float alpha1 = toDegrees(a1);
      float alpha2 = toDegrees(a2);
      float alpha3 = toDegrees(a3);

      theta1 = alpha1 + alpha2;
      theta2 = alpha3 - 180;

      x1 = l1 * cos(toRadians(theta1));
      y1 = l1 * sin(toRadians(theta1));
    }

  public:
    Robot2DOF(float _x, float _y, float _l1, float _l2) {
      x = _x;
      y = _y;
      l1 = _l1;
      l2 = _l2;
      servo1.attach(9); // Attach servo 1 to pin 9
      servo2.attach(10); // Attach servo 2 to pin 10
    }

    void simulate() {
      float theta1, theta2, x1, y1;
      float center_x = 15;
      float center_y = 10;
      float radius = 5;
      int num_points = 50;
      float angle_step = 360.0 / num_points;

      for (int i = 0; i < num_points; i++) {
        float angle_degrees = i * angle_step;
        float angle_radians = toRadians(angle_degrees);
        float target_x = center_x + radius * cos(angle_radians);
        float target_y = center_y + radius * sin(angle_radians);

        inverseKinematics(target_x, target_y, theta1, theta2, x1, y1);
        Serial.print("Theta1: ");
        Serial.print(theta1);
        Serial.print(" degrees, Theta2: ");
        Serial.println(theta2);

        Serial.print("x1: ");
        Serial.print(x1);
        Serial.print(", y1: ");
        Serial.println(y1);
        
        Serial.print("x2: ");
        Serial.print(target_x);
        Serial.print(" y2: ");
        Serial.println(target_y);

        // Move servo motors based on calculated angles
        servo1.write(theta1);
        servo2.write(theta2);

        delay(10); // Delay between each step
      }
    }
};

void setup() {
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  Robot2DOF robot(20, 0, 8, 16); // Create robot instance
  robot.simulate(); // Run simulation
  delay(100000); // Delay before running simulation again
}
