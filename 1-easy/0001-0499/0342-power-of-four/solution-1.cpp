#include <bits/stdc++.h>
using namespace std;

// using logarithm

class Solution
{
public:
    bool isPowerOfFour(int n)
    {
        if (n <= 0)
            return false;

        if (n == 1)
            return true;

        double res = log(n) / log(4);

        return res == int(res);
    }
};

int main()
{
    Solution sol;
    return 0;
}