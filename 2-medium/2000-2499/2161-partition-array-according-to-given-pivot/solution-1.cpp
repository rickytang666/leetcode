#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> pivotArray(vector<int> &nums, int pivot)
    {
        vector<int> smaller, equal, bigger, ans;
        for (const int &n : nums)
        {
            if (n < pivot)
                smaller.push_back(n);
            else if (n == pivot)
                equal.push_back(n);
            else
                bigger.push_back(n);
        }
        ans.insert(ans.end(), smaller.begin(), smaller.end());
        ans.insert(ans.end(), equal.begin(), equal.end());
        ans.insert(ans.end(), bigger.begin(), bigger.end());

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