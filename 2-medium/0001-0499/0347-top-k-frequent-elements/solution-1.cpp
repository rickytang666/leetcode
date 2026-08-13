#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> &a, pair<int, int> &b)
{
    return a.second > b.second;
}

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> m;
        for (int n : nums)
        {
            m[n]++;
        }
        vector<pair<int, int>> v;
        for (auto p : m)
        {
            v.emplace_back(p.first, p.second);
        }
        sort(v.begin(), v.end(), cmp);
        vector<int> ans;
        for (int i = 0; i < k; ++i)
        {
            ans.push_back(v[i].first);
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;
    vector<int> result = sol.topKFrequent(nums, k);
    for (int num : result)
    {
        cout << num << " ";
    }
    cout << endl;
    // Expected output: 1 2 (or any order of the top 2 frequent elements)
    return 0;
}