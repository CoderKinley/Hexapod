#include <math.h>

void inverseKinematics(float* theta1, float* theta2, float* theta3) {
    float x = 16;
    float y = 16;
    float z = 8;
    float a1 = 4;
    float a2 = 8;
    float a3 = 16;

    float theta1_temp = atan2(y, x) * 180 / M_PI;
    float a4 = sqrt(pow((x - a1), 2) + pow(a3, 2));
    float phi3 = acos(((pow(a2, 2)) + (pow(a4, 2)) - (pow(a3, 2))) / (2 * a2 * a4));
    float phi2 = asin(z / a4);
    phi3 = phi3 * 180 / M_PI;
    phi2 = phi2 * 180 / M_PI;
    float theta2_temp = phi2 + phi3;
    float val = ((pow(a2, 2)) + (pow(a3, 2)) - (pow(a4, 2))) / (2 * a2 * a3);
    float phi1 = acos(val) * 180 / M_PI;
    float theta3_temp = phi1 - 180;
  
    *theta1 = theta1_temp;
    *theta2 = theta2_temp;
    *theta3 = theta3_temp;
}