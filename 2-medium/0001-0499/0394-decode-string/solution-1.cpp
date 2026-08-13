#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string decodePos(const string &s, int &i)
    {
        string ans;
        while (i < s.size() && s[i] != ']')
        {
            if (!isdigit(s[i]))
                ans += s[i++];
            else
            {
                int n = 0;
                while (i < s.size() && isdigit(s[i]))
                {
                    n = n * 10 + (s[i++] - '0');
                }
                ++i; // meet '['
                string str = decodePos(s, i);
                ++i; // meet ']'

                // put the string to answer
                while (n-- > 0)
                    ans += str;
            }
        }

        return ans;
    }
    string decodeString(string s)
    {
        int i = 0;
        return decodePos(s, i);
    }
};

int main()
{
    Solution sol;
    string s = "3[a2[c]]";
    cout << sol.decodeString(s) << endl; // expected output: "accaccacc"
    return 0;
}