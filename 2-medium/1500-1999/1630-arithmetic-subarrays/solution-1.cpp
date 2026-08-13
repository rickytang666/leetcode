#include <bits/stdc++.h>
using namespace std;

// sorting the subarray and checking if it is arithmetic
// time complexity: O(m * n log n) where m is the number of queries and n is the average size of the subarrays

class Solution
{
public:
    bool is_arithmetic(vector<int> &v)
    {
        if (v.size() == 2)
            return true;
        int diff = v[1] - v[0];
        for (int i = 2; i < v.size(); ++i)
        {
            if (v[i] - v[i - 1] != diff)
                return false;
        }
        return true;
    }

    vector<bool> checkArithmeticSubarrays(vector<int> &nums, vector<int> &l, vector<int> &r)
    {
        vector<bool> ans;
        int m = l.size();
        for (int i = 0; i < m; ++i)
        {
            vector<int> v(nums.begin() + l[i], nums.begin() + r[i] + 1);
            sort(v.begin(), v.end());
            ans.push_back(is_arithmetic(v));
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {4, 6, 5, 9, 3, 7};
    vector<int> l = {0, 0, 2};
    vector<int> r = {2, 3, 5};
    vector<bool> result = sol.checkArithmeticSubarrays(nums, l, r);
    for (bool res : result)
    {
        cout << (res ? "true" : "false") << " ";
    }
    cout << endl;
    return 0;
}