#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> sortMatrix(vector<vector<int>> &grid)
    {
        int n = grid.size();
        map<int, vector<int>> m;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
                m[i - j].push_back(grid[i][j]);
        }

        for (auto &p : m)
        {
            if (p.first < 0)
                sort(p.second.begin(), p.second.end());
            else
                sort(p.second.begin(), p.second.end(), greater<int>());
        }

        for (int i = n - 1; i >= 0; --i)
        {
            for (int j = n - 1; j >= 0; --j)
            {
                grid[i][j] = m[i - j].back();
                m[i - j].pop_back();
            }
        }

        return grid;
    }
};

int main()
{
    vector<vector<int>> grid = {{1, 7, 3}, {4, 8, 5}, {9, 2, 6}};
    auto ans = Solution().sortMatrix(grid);
    for (const auto &row : ans)
    {
        for (const auto &num : row)
            cout << num << " ";
        cout << "\n";
    }
    return 0;
}