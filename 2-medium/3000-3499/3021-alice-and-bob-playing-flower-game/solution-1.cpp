#include <bits/stdc++.h>
using namespace std;

// using math, ans = floor(n * m/2)

class Solution
{
public:
    long long flowerGame(int n, int m)
    {
        return 1LL * n * m / 2; // long long
    }
};

int main()
{
    int n = 3, m = 3;
    cout << Solution().flowerGame(n, m) << "\n"; // expected: 4
    return 0;
}