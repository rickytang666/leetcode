/*
 * @lc app=leetcode id=686 lang=c
 *
 * [686] Repeated String Match
 */

// @lc code=start
#include <stdbool.h>

int repeatedStringMatch(char *a, char *b)
{
    int a_len = strlen(a);
    int b_len = strlen(b);

    int bound = (b_len + a_len - 1) / a_len;

    for (int k = 0; k < 2; k++)
    {
        int total_len = (bound + k) * a_len;

        for (int i = 0; i <= total_len - b_len; i++)
        {
            bool match = true;

            for (int j = 0; j < b_len; j++)
            {
                if (a[(i + j) % a_len] != b[j])
                {
                    match = false;
                    break;
                }
            }

            if (match)
                return bound + k;
        }
    }

    return -1;
}
// @lc code=end
