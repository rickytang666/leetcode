#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string removeStars(string s)
    {
        string ans = "";
        for (char c : s)
        {
            if (c == '*')
                ans.pop_back();
            else
                ans += c;
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    string s = "leet**cod*e";
    cout << sol.removeStars(s) << endl;
    return 0;
}