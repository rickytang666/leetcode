#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> findDiagonalOrder(vector<vector<int>> &mat)
    {
        int m = mat.size(), n = mat[0].size();
        vector<int> ans, v;
        // the head of a diagonal can only be first row or last column
        for (int h = 0; h < m + n - 1; ++h)
        {
            v.clear();
            // identify the location of head (1st row or last col)
            int r = -1, c = -1;
            if (h < n)
            {
                r = 0;
                c = h;
            }
            else
            {
                r = h - n + 1;
                c = n - 1;
            }

            while (r < m && c >= 0)
            {
                v.push_back(mat[r++][c--]);
            }

            if (h % 2 == 0)
                reverse(v.begin(), v.end());
            ans.reserve(ans.size() + v.size());
            ans.insert(ans.end(), v.begin(), v.end());
        }
        return ans;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}