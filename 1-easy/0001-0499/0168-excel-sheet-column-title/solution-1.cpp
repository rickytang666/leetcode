#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string convertToTitle(int n)
    {
        string ans;
        while (n > 0)
        {
            // constrain n to be within the range of 1 to 26
            int remainder = (n - 1) % 26 + 1;
            char c = 'A' + remainder - 1;
            // cout << "Current n: " << n << ", Remainder: " << remainder << ", Character: " << c << endl;
            ans.insert(0, 1, c);
            n -= remainder;
            n /= 26;
        }
        return ans;
    }
};

int main()
{
    Solution solution;
    int n = 701;
    string result = solution.convertToTitle(n);
    cout << "Column title: " << result << endl;
    return 0;
}