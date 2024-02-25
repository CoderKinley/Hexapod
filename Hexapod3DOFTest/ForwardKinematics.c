#include <math.h>

void calculateTransformationMatrix(float matrix[4][4], float row[4]) {
  matrix[0][0] = cos(row[0]);
  matrix[0][1] = -sin(row[0]) * cos(row[1]);
  matrix[0][2] = sin(row[0]) * sin(row[1]);
  matrix[0][3] = row[2] * cos(row[0]);
  
  matrix[1][0] = sin(row[0]);
  matrix[1][1] = cos(row[0]) * cos(row[1]);
  matrix[1][2] = -cos(row[0]) * sin(row[1]);
  matrix[1][3] = row[2] * sin(row[0]);
  
  matrix[2][0] = 0;
  matrix[2][1] = sin(row[1]);
  matrix[2][2] = cos(row[1]);
  matrix[2][3] = row[3];
  
  matrix[3][0] = 0;
  matrix[3][1] = 0;
  matrix[3][2] = 0;
  matrix[3][3] = 1;
}

void matrixMultiplication(float matrixA[4][4], float matrixB[4][4], float result[4][4]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      result[i][j] = 0;
      for (int k = 0; k < 4; k++) {
        result[i][j] += matrixA[i][k] * matrixB[k][j];
      }
    }
  }
}
