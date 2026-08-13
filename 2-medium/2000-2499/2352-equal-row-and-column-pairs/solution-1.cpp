#include <bits/stdc++.h>
using namespace std;

// hashmap solution

class Solution
{
public:
    int equalPairs(vector<vector<int>> &grid)
    {
        map<vector<int>, int> m;

        int ans = 0, n = grid.size();

        for (int row = 0; row < n; ++row)
        {
            m[grid[row]]++;
        }

        for (int col = 0; col < n; ++col)
        {
            vector<int> v;
            for (int row = 0; row < n; ++row)
            {
                v.push_back(grid[row][col]);
            }
            ans += m[v];
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> grid = {
        {1, 2, 3},
        {2, 3, 1},
        {3, 1, 2}};
    cout << sol.equalPairs(grid) << endl; // expected output: 3
    return 0;
}