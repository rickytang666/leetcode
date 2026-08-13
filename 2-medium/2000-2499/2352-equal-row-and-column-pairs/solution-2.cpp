#include <bits/stdc++.h>
using namespace std;

// brute force solution O(n^3)

class Solution
{
public:
    int equalPairs(vector<vector<int>> &grid)
    {
        int ans = 0, n = grid.size();

        for (int row = 0; row < n; ++row)
        {

            for (int col = 0; col < n; ++col)
            {
                bool equal = true;

                for (int k = 0; k < n; ++k)
                {
                    if (grid[row][k] != grid[k][col])
                    {
                        equal = false;
                        break;
                    }
                }

                if (equal)
                    ans++;
            }
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