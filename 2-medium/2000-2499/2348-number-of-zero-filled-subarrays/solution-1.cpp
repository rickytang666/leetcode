#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    long long zeroFilledSubarray(vector<int> &nums)
    {
        long long span = 0;
        long long ans = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] != 0)
            {
                if (span > 0)
                {
                    ans += (span) * (span + 1) / 2;
                    span = 0;
                }
            }
            else
            {
                ++span;
            }
        }

        if (span > 0)
        {
            ans += span * (span + 1) / 2;
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {0, 0, 0, 2, 0, 0};
    cout << sol.zeroFilledSubarray(nums) << endl;
    return 0;
}