#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxOperations(vector<int> &nums, int k)
    {
        int ans = 0, left = 0, right = nums.size() - 1;

        sort(nums.begin(), nums.end());

        while (left < right)
        {
            if (nums[left] + nums[right] == k)
                ans++, left++, right--;
            else if (nums[left] + nums[right] < k)
                left++;
            else
                right--;
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    int k = 5;
    cout << sol.maxOperations(nums, k) << endl; // expected output: 2
    return 0;
}