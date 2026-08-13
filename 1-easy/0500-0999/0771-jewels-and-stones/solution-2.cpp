#include <bits/stdc++.h>
using namespace std;

// map solution

class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        int cnt = 0;
        unordered_map<char, int> m;
        for (const char &c : stones)
            m[c]++;
        for (const char &c : jewels)
            cnt += m[c];

        return cnt;
    }
};

int main()
{
    Solution sol;
    string jewels = "aA", stones = "aAAbbbb";
    cout << sol.numJewelsInStones(jewels, stones) << endl;
    return 0;
}