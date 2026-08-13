#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &v)
    {
        int n = v.size();
        int left = 0, right = n - 1;
        int ans = 0;

        while (left < right)
        {
            int area = 0;
            if (v[left] <= v[right])
            {
                area = v[left] * (right - left);
                left++;
            }
            else
            {
                area = v[right] * (right - left);
                right--;
            }

            ans = max(ans, area);
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << sol.maxArea(v) << endl; // expected output: 49
    return 0;
}