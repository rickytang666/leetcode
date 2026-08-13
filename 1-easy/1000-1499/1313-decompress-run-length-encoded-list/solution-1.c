/*
 * @lc app=leetcode id=1313 lang=c
 *
 * [1313] Decompress Run-Length Encoded List
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

int *decompressRLElist(int *nums, int numsSize, int *returnSize)
{
    int size = 0;
    for (int i = 0; i < numsSize; i += 2)
        size += nums[i];
    int *ans = malloc(size * sizeof(int));
    int pos = 0;
    for (int i = 0; i < numsSize; i += 2)
    {
        int freq = nums[i], val = nums[i + 1];
        for (int j = 0; j < freq; ++j)
        {
            ans[pos++] = val;
        }
    }
    *returnSize = size;
    return ans;
}
// @lc code=end
