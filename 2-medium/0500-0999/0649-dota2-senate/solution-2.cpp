#include <bits/stdc++.h>
using namespace std;

// beats 43.79%

class Solution
{
public:
    string predictPartyVictory(string senate)
    {
        int r_ban = 0, d_ban = 0;
        queue<int> q(senate.begin(), senate.end());
        while (!q.empty())
        {
            if (q.front() == 'R')
            {
                if (r_ban > 0)
                    r_ban--; // skip
                else
                {
                    d_ban++;
                    q.push('R'); // keep
                }
            }
            else
            {
                if (d_ban > 0)
                    d_ban--; // skip
                else
                {
                    r_ban++;
                    q.push('D'); // keep
                }
            }
            q.pop();
            if (r_ban == q.size())
                return "Dire";
            if (d_ban == q.size())
                return "Radiant";
        }
        return "WTF"; // all cases must be covered in the loop
    }
};

int main()
{
    string senate = "RDD";
    cout << Solution().predictPartyVictory(senate) << endl; // expected output: "Dire"
    return 0;
}