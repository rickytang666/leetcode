#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &v)
    {
        int n = v.size();
        vector<vector<int>> ans;
        sort(v.begin(), v.end());

        for (int i = 0; i < n - 2; ++i)
        {
            if (i > 0 && v[i - 1] == v[i])
                continue;

            int j = i + 1, k = n - 1;

            while (j < k)
            {
                int sum = v[i] + v[j] + v[k];
                if (sum == 0)
                {
                    ans.push_back({v[i], v[j], v[k]});
                    ++j; // force move the index
                    while (v[j] == v[j - 1] && j < k)
                    {
                        ++j;
                    }
                }
                else if (sum > 0)
                {
                    --k;
                }
                else
                {
                    ++j;
                }
            }
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> result = sol.threeSum(v);
    for (const auto &triplet : result)
    {
        cout << "[" << triplet[0] << ", " << triplet[1] << ", " << triplet[2] << "]\n";
    }
    // expected output: [-1, -1, 2], [-1, 0, 1]
    return 0;
}