#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        string n;
        for (char c : s)
        {
            if (isalnum(c))
            {
                n += tolower(c);
            }
        }

        int i = 0, j = n.length() - 1;
        while (i <= j)
        {
            if (n[i++] != n[j--])
                return false;
        }
        return true;
    }
};

int main()
{
    string s = "A man, a plan, a canal: Panama";
    Solution sol;
    cout << (sol.isPalindrome(s) ? "true" : "false") << endl;
    return 0;
}