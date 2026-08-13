#include <bits/stdc++.h>
using namespace std;

// beats 43.79%

class Solution
{
public:
    string predictPartyVictory(string senate)
    {
        int n = int(senate.size());
        queue<int> rad, dir;
        // assign senates to parties
        for (int i = 0; i < n; ++i)
        {
            if (senate[i] == 'R')
                rad.push(i);
            else
                dir.push(i);
        }
        while (!rad.empty() && !dir.empty())
        {
            // fight
            int r = rad.front(), d = dir.front();
            rad.pop();
            dir.pop();
            ++n;
            if (r < d)
                rad.push(n);
            else
                dir.push(n);
        }
        if (rad.empty())
            return "Dire";
        else
            return "Radiant";
    }
};

int main()
{
    string senate = "RDD";
    cout << Solution().predictPartyVictory(senate) << endl; // expected output: "Dire"
    return 0;
}