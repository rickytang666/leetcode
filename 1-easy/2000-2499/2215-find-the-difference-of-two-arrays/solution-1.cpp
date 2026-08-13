#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> findDifference(vector<int> &nums1, vector<int> &nums2)
    {
        set<int> s1, s2;
        for (int n : nums1)
            s1.insert(n);
        for (int n : nums2)
            s2.insert(n);
        vector<int> d1, d2;
        set_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(d1));
        set_difference(s2.begin(), s2.end(), s1.begin(), s1.end(), back_inserter(d2));
        return {d1, d2};
    }
};

int main()
{
    Solution sol;
    vector<int> nums1 = {1, 2, 3}, num2 = {2, 4, 6};
    vector<vector<int>> result = sol.findDifference(nums1, num2);
    for (const auto &vec : result)
    {
        for (int num : vec)
            cout << num << " ";
        cout << endl;
    }
    return 0;
}