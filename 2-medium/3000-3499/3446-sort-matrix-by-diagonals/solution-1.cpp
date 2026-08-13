#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> sortMatrix(vector<vector<int>> &grid)
    {
        int n = grid.size();
        for (int h = 0; h < n * 2 - 1; ++h)
        {
            int r = -1, c = -1;
            if (h < n)
            {
                r = n - h - 1;
                c = 0;
            }
            else
            {
                r = 0;
                c = h - n + 1;
            }

            vector<pair<int, int>> indices;
            vector<int> v;
            while (r < n && c < n)
            {
                indices.emplace_back(r, c);
                v.push_back(grid[r++][c++]);
            }

            if (h < n)
                sort(v.begin(), v.end(), greater<int>());
            else
                sort(v.begin(), v.end());

            for (int i = 0; i < indices.size(); ++i)
            {
                grid[indices[i].first][indices[i].second] = v[i];
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