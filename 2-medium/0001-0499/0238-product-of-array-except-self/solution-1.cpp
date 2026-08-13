#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &v)
    {
        int n = v.size();
        vector<int> ans(n, 0);
        int pro = 1, cnt_0 = 0, index = -1;
        for (int i = 0; i < n; ++i)
        {
            if (v[i] == 0)
            {
                cnt_0++;
                index = i;
            }
            else
            {
                pro *= v[i];
            }
        }
        if (cnt_0 > 1)
            return ans; // all zeroes guaranteed
        if (cnt_0 == 1)
        {
            ans[index] = pro;
            return ans;
        }

        for (int i = 0; i < n; ++i)
        {
            ans[i] = pro / v[i];
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {1, 2, 3, 4};
    vector<int> result = sol.productExceptSelf(v);
    for (int num : result)
    {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}