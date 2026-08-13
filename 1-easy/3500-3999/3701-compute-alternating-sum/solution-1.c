int alternatingSum(int *nums, int numsSize)
{
    int id = 1;

    int sum = 0;

    for (int i = 0; i < numsSize; ++i)
    {
        sum += id * nums[i];
        id *= -1;
    }

    return sum;
}