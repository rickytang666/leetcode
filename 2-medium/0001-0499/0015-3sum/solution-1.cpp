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
        unordered_map<int, int> m;

        for (int i = 0; i < n; ++i)
        {
            m[v[i]] = i;
        }

        for (int i = 0; i < n - 2; ++i)
        {
            if (i > 0 && v[i - 1] == v[i])
                continue;
            int y_z = -v[i];
            for (int j = i + 1; j < n; ++j)
            {
                if (j > i + 1 && v[j - 1] == v[j])
                    continue;
                int z = y_z - v[j];
                if (z < v[j])
                    break;
                if (m.contains(z) && m[z] > j)
                {
                    ans.push_back({v[i], v[j], z});
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
    // Example output: [-1, -1, 2], [-1, 0, 1]
    return 0;
}