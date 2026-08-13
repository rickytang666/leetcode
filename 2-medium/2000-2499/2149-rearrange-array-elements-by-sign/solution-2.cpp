#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> rearrangeArray(vector<int> &v)
    {
        int n = v.size();
        vector<int> ans(n, 0);
        int pi = 0, ni = 1;
        for (int i = 0; i < n; ++i)
        {
            if (v[i] > 0)
            {
                ans[pi] = v[i];
                pi += 2;
            }
            else
            {
                ans[ni] = v[i];
                ni += 2;
            }
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {3, 1, -2, -5, 2, -4};
    vector<int> result = sol.rearrangeArray(v);
    for (int num : result)
    {
        cout << num << " ";
    }
    cout << endl; // expected output: 3 -2 1 -5 2 -4
    return 0;
}