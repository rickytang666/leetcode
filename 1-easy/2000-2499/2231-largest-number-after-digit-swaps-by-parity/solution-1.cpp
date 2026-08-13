#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int largestInteger(int num)
    {
        // the odd-even sequence is retained
        string s = to_string(num);
        priority_queue<int> odds, evens;
        int n = s.size();

        for (int i = 0; i < n; ++i)
        {
            int digit = s[i] - '0';
            if (digit % 2)
                odds.push(digit);
            else
                evens.push(digit);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i)
        {
            ans *= 10;
            if ((s[i] - '0') % 2)
            {
                ans += odds.top();
                odds.pop();
            }
            else
            {
                ans += evens.top();
                evens.pop();
            }
        }

        return ans;
    }
};

int main()
{
    int num = 1234;
    cout << Solution().largestInteger(num) << "\n"; // expected: 3412
    return 0;
}