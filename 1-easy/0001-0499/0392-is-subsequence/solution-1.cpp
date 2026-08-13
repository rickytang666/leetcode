#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int i = 0, j = 0, cnt = 0;

        while (j < t.size() && i < s.size())
        {
            if (t[j] == s[i])
            {
                ++cnt;

                if (cnt == s.size())
                    return true;

                ++i;
            }

            ++j;
        }

        return cnt == s.size();
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}