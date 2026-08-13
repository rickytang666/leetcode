#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int get_next(int num)
    {
        string s = to_string(num);
        int res = 0;
        for (char c : s)
        {
            res += pow(c - '0', 2);
        }
        return res;
    }

    bool isHappy(int n)
    {
        unordered_set<int> seen;

        while (!seen.contains(n))
        {
            seen.insert(n);
            n = get_next(n);
            if (n == 1)
                return true;
        }

        return false;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}