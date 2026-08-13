#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxOperations(vector<int> &nums, int k)
    {
        int ans = 0;
        unordered_map<int, int> m;
        unordered_set<int> seen;
        for (int n : nums)
            m[n]++;

        for (auto p : m)
        {
            int key = p.first;
            if (key * 2 == k)
            {
                // pair with itself
                ans += p.second / 2;
            }
            else
            {
                // pair with a distinct
                if (seen.contains(key))
                    continue;
                seen.insert(key);
                int other = k - key;
                if (m.contains(other))
                {
                    ans += min(p.second, m[other]);
                    seen.insert(other);
                }
            }
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    int k = 5;
    cout << sol.maxOperations(nums, k) << endl; // expected output: 2
    return 0;
}