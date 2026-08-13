#include <bits/stdc++.h>
using namespace std;

// NOT ACCEPTED: too slow TLE at 14/43 😭 (this is basically brute force)

/*
pour 100 mL from type A and 0 mL from type B
pour 75 mL from type A and 25 mL from type B
pour 50 mL from type A and 50 mL from type B
pour 25 mL from type A and 75 mL from type B
*/

class Solution
{
public:
    double prob(int A, int B)
    {
        if (A <= 0 && B <= 0)
            return 0.5;
        else if (A <= 0)
            return 1;
        else if (B <= 0)
            return 0;

        double ans = 0;
        int a = 0, b = 0;

        // op 1
        a = A - 100, b = B;
        ans += 0.25 * prob(a, b);

        // op 2
        a = A - 75, b = B - 25;
        ans += 0.25 * prob(a, b);

        // op 3
        a = A - 50, b = B - 50;
        ans += 0.25 * prob(a, b);

        // op 4
        a = A - 25, b = B - 75;
        ans += 0.25 * prob(a, b);

        return ans;
    }

    double soupServings(int n)
    {
        return prob(n, n);
    }
};

int main()
{
    Solution sol;
    int n = 100;
    cout << sol.soupServings(n) << endl;
    return 0;
}