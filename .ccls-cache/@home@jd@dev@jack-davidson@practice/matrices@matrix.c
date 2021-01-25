#include <stdio.h>

int matrix1[3][3] = {
	{1, 2, 3},
	{4, 5, 6},
	{7, 8, 9},
};

int matrix2[3][3] = {
	{7, 8, 9},
	{4, 5, 6},
	{1, 2, 3},
};

int newmatrix[3][3];

int main()
{
	/* the following lines multiply the first column of matrix1
	 * by the first row of matrix2.
	 */
	int product1;
	int product2;
	product1 = matrix1[0][0] * matrix1[1][0] * matrix1[2][0];
	product2 = matrix2[0][0] * matrix2[0][1] * matrix2[0][2];
	newmatrix[0][0] = product1 * product2;
	printf("%i", newmatrix[0][0]);
	return 0;
}
