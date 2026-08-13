#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int largestAltitude(vector<int> &gain)
    {
        int ans = 0, sum = 0;
        for (int n : gain)
        {
            sum += n;
            if (n > 0)
                ans = max(ans, sum);
        }
        return ans;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}