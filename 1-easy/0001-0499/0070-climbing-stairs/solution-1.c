/*
 * @lc app=leetcode id=70 lang=c
 *
 * [70] Climbing Stairs
 */

// @lc code=start
long long tr(int n, long long a, long long b)
{
    if (n == 0)
        return a;
    return tr(n - 1, b, a + b);
}

long long climbStairs(int n)
{
    return tr(n, 1, 1);
}
// @lc code=end
