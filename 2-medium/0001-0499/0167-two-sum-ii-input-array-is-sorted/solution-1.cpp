#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &v, int target)
    {
        int left = 0, right = v.size() - 1;
        while (left < right)
        {
            int sum = v[left] + v[right];

            if (sum == target)
                return {left + 1, right + 1};
            else if (sum > target)
                --right;
            else
                ++left;
        }
        return {-1, -1};
    }
};

int main()
{
    Solution sol;
    vector<int> v = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = sol.twoSum(v, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl; // expected output: [1, 2]
    return 0;
}