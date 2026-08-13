#include <bits/stdc++.h>
using namespace std;

// sneaky method: fully make use of contraints (-1000 <= nums[i] <= 1000)

class Solution
{
public:
    vector<vector<int>> findDifference(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> v1(2001, 0), v2(2001, 0);
        for (int n : nums1)
            v1[n + 1000]++;
        for (int n : nums2)
            v2[n + 1000]++;
        vector<vector<int>> ans(2, vector<int>());
        for (int i = 0; i < 2001; ++i)
        {
            if (v1[i] > 0 && v2[i] == 0)
                ans[0].push_back(i - 1000);
            if (v2[i] > 0 && v1[i] == 0)
                ans[1].push_back(i - 1000);
        }
        return ans;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}