#include <bits/stdc++.h>
using namespace std;

// without sorting or hashing
// O(n) time and O(n) space for each query

class Solution
{
public:
    bool is_arithmetic(vector<int> &v, int l, int r)
    {
        auto p = minmax_element(v.begin() + l, v.begin() + r + 1);
        int minN = *p.first, maxN = *p.second;
        int diff = maxN - minN, n = r - l + 1;
        if (diff == 0)
            return true;
        if (diff % (r - l) != 0)
            return false;
        int d = diff / (r - l); // common diff
        vector<int> terms(n, 0);

        for (int i = l; i <= r; ++i)
        {
            int x = v[i] - minN;
            if (x % d != 0)
                return false;
            int j = x / d;
            if (terms[j])
                return false; // cannot have duplicates in non-constant sequence
            terms[j] = 1;
        }

        return true;
    }

    vector<bool> checkArithmeticSubarrays(vector<int> &nums, vector<int> &l, vector<int> &r)
    {
        vector<bool> ans;
        int m = l.size();
        for (int i = 0; i < m; ++i)
        {
            ans.push_back(is_arithmetic(nums, l[i], r[i]));
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
    // Expected output: true false true
    return 0;
}