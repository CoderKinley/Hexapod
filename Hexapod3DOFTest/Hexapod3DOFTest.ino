#include <math.h>
#include "InverseKinematics.c"
#include "ForwardKinematics.c"

// Joint lengths 
float r1 = 4;
float r2 = 8;
float r3 = 16;

// Joint angles
float theta1 = 38.66 * PI / 180.0; // Convert degrees to radians
float theta2 = 40.65 * PI / 180.0; // Convert degrees to radians
float theta3 = -41.41 * PI / 180.0; // Convert degrees to radians

// Angle between z-axes
float alpha1 = 90 * PI / 180.0; // Convert degrees to radians
float alpha2 = 0 * PI / 180.0; // Convert degrees to radians
float alpha3 = 0 * PI / 180.0; // Convert degrees to radians

void setup() {
  Serial.begin(9600);
  //  calling the inverkinematics file there
  float theta_1, theta_2, theta_3;
  inverseKinematics(&theta_1, &theta_2, &theta_3);
  Serial.println();  
  Serial.print("Theta1: ");
  Serial.print(theta_1);
  Serial.print(", Theta2: ");
  Serial.print(theta_2);
  Serial.print(", Theta3: ");
  Serial.println(theta_3);

  theta_1 = theta_1 * PI / 180.0; 
  theta_2 = theta_2 * PI / 180.0; 
  theta_3 = theta_3 * PI / 180.0; 

  
  // Declaring the Denivit Hertenbert 
  // Forward Kinematics to see the correction value
  float t[3][4] = {{theta_1, alpha1, r1, 0},
                   {theta_2, alpha2, r2, 0},
                   {theta_3, alpha3, r3, 0}};

  // Transformation matrices
  float t01[4][4];
  float t12[4][4];
  float t23[4][4];

  calculateTransformationMatrix(t01, t[0]);
  calculateTransformationMatrix(t12, t[1]);
  calculateTransformationMatrix(t23, t[2]);

  // Calculate t02 and t03
  float t02[4][4];
  float t03[4][4];
  matrixMultiplication(t01, t12, t02);
  matrixMultiplication(t02, t23, t03);

  // Print the rounded matrices
  Serial.println("t01_rounded:");
  printMatrix(t01);
  Serial.println();
  
  Serial.println("t02_rounded:");
  printMatrix(t02);
  Serial.println();
  
  Serial.println("t03_rounded (Homogenous Matrix frame 0 to frame 2):");
  printMatrix(t03);

}
void loop() {
  // Nothing to do here
  // wave gate
  // ripple gate
  // tripod gate
  // rotation gate implementation
}

void printMatrix(float matrix[4][4]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      Serial.print(matrix[i][j], 3);
      Serial.print("\t");
    }
    Serial.println();
  }
}
