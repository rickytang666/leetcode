#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool same(int a, int b)
    {
        string p = to_string(a), q = to_string(b);

        if (p.size() != q.size())
            return false;

        vector<int> v1(10, 0), v2(10, 0);

        for (char c : p)
        {
            v1[c - '0']++;
        }

        for (char c : q)
        {
            v2[c - '0']++;
        }

        return v1 == v2;
    }

    bool reorderedPowerOf2(int n)
    {
        for (int i = 0; i < 31; ++i)
        {
            if (same(n, pow(2, i)))
                return true;
        }

        return false;
    }
};

int main()
{
    Solution sol;
    int n = 10;
    bool result = sol.reorderedPowerOf2(n);
    cout << (result ? "True" : "False") << endl; // expected output: False
    return 0;
}