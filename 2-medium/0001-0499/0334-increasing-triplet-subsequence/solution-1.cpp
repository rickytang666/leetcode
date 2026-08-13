#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool increasingTriplet(vector<int> &nums)
    {
        if (nums.size() < 3)
            return false;

        int a = INT_MAX, b = INT_MAX; // smallest and 2nd-smallest (from left to right order)

        for (int num : nums)
        {
            if (num <= a)
                a = num;
            else if (num <= b)
                b = num;
            else
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