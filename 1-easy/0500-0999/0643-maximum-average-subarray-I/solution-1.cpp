#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double findMaxAverage(vector<int> &nums, int k)
    {
        double curr = accumulate(nums.begin(), nums.begin() + k, 0.0), ans = curr;
        for (int i = k; i < nums.size(); ++i)
            ans = max(ans, curr += nums[i] - nums[i - k]);
        return ans / k;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 12, -5, -6, 50, 3};
    int k = 4;
    cout << sol.findMaxAverage(nums, k) << endl; // expected output: 12.75
    return 0;
}