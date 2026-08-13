#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double *convertTemperature(double celsius, int *returnSize)
{
    double *answer = malloc(2 * sizeof(double));
    answer[0] = celsius + 273.15;
    answer[1] = celsius * 1.80 + 32.00;
    *returnSize = 2;
    return answer;
}