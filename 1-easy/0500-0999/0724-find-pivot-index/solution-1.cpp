#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int n = nums.size();
        long long rightSum = accumulate(nums.begin(), nums.end(), 0), leftSum = 0;
        for (int i = 0; i < n; ++i)
        {
            rightSum -= nums[i];
            if (i > 0)
                leftSum += nums[i - 1];
            if (leftSum == rightSum)
                return i;
        }

        return -1;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}