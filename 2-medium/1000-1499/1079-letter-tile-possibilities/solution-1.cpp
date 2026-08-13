#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int dfs(vector<int> v)
    {

        int ans = 0;

        if (v.size() != 26)
            return ans;

        for (int i = 0; i < v.size(); ++i)
        {
            if (v[i])
            {
                ans++;
                v[i]--;
                ans += dfs(v);
                v[i]++; // revert
            }
        }

        return ans;
    }

    int numTilePossibilities(string tiles)
    {
        vector<int> v(26, 0);

        for (char c : tiles)
            v[c - 'A']++;

        return dfs(v);
    }
};

int main()
{
    Solution sol;
    string tiles = "AAB";
    cout << sol.numTilePossibilities(tiles) << endl; // expected output: 8
    return 0;
}