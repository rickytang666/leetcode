#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int longestOnes(vector<int> &nums, int k)
    {
        int l = 0, r = 0;
        while (r < nums.size())
        {
            if (!nums[r])
                --k;

            if (k < 0)
            {
                if (!nums[l++])
                    ++k;
            }

            ++r;
        }
        return r - l;
    }
};

int main()
{
    vector<int> nums = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
    int k = 2;
    cout << Solution().longestOnes(nums, k) << endl;
    return 0;
}