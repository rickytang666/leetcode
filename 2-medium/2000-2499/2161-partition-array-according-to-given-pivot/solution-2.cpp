#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> pivotArray(vector<int> &nums, int pivot)
    {
        int n = nums.size();
        int left = 0, right = n - 1;
        vector<int> ans(n, 0);
        for (int i = 0, j = n - 1; i < n && j >= 0; ++i, --j)
        {
            if (nums[i] < pivot)
            {
                ans[left] = nums[i];
                ++left;
            }

            if (nums[j] > pivot)
            {
                ans[right] = nums[j];
                --right;
            }
        }

        while (left <= right)
        {
            ans[left] = pivot;
            ++left;
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {9, 12, 5, 10, 14, 3, 10};
    int pivot = 10;
    vector<int> result = sol.pivotArray(nums, pivot);
    for (int num : result)
    {
        cout << num << " ";
    }
    cout << endl;
    // Expected: 9 5 3 10 10 12 14
    return 0;
}