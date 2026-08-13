#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        int cnt = 0;
        for (char c : stones)
        {
            if (jewels.contains(c))
                ++cnt;
        }
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