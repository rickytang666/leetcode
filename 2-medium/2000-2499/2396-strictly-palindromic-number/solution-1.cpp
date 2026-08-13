#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string to_base(int n, int base)
    {
        if (n == 0)
            return "0";
        string digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string ans;
        while (n > 0)
        {
            int rem = n % base;
            ans += digits[rem];
            n /= base;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
    bool is_palindromic(string s)
    {
        int i = 0, j = s.length() - 1;
        while (i < j)
        {
            if (s[i++] != s[j--])
                return false;
        }
        return true;
    }
    bool isStrictlyPalindromic(int n)
    {
        for (int b = 2; b <= n - 2; ++b)
        {
            if (!is_palindromic(to_base(n, b)))
                return false;
        }
        return true;
    }
};

int main()
{
    Solution sol;
    int n = 9; // Example input
    bool result = sol.isStrictlyPalindromic(n);
    cout << (result ? "True" : "False") << endl; // Output result
    // Expected: false
    return 0;
}