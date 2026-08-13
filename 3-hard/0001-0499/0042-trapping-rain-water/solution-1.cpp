#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &v)
    {
        int ans = 0, left = 0, right = v.size() - 1, level = 0;
        while (left < right)
        {
            int lower = v[v[left] < v[right] ? left++ : right--];
            level = max(level, lower);
            ans += level - lower;
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3};
    cout << sol.trap(v) << endl; // expected: 83
    return 0;
}