#include <bits/stdc++.h>
using namespace std;

// solution 2 (not very efficient)

class Solution
{
public:
    int choose(int n, int k)
    {
        if (k == 0)
            return 1;
        return (n * choose(n - 1, k - 1)) / k;
    }

    vector<vector<int>> generate(int n)
    {
        vector<vector<int>> v;
        for (int i = 0; i < n; ++i)
        {
            vector<int> a;
            for (int j = 0; j <= i; ++j)
            {
                a.push_back(choose(i, j));
            }
            v.push_back(a);
        }
        return v;
    }
};

int main()
{
    Solution sol;
    int numRows = 5; // Example input
    vector<vector<int>> result = sol.generate(numRows);
    for (const auto &row : result)
    {
        for (int num : row)
        {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}