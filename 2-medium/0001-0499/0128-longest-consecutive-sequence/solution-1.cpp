#include <bits/stdc++.h>
using namespace std;

// looked up a solution 😢

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> s(nums.begin(), nums.end());
        int ans = 0;

        for (int num : s)
        {
            if (s.find(num - 1) == s.end())
            {
                int len = 1;

                while (s.find(num + len) != s.end())
                {
                    len++;
                }

                ans = max(ans, len);
            }
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {100, 4, 200, 1, 3, 2};
    cout << sol.longestConsecutive(nums) << endl; // expected output: 4
    return 0;
}