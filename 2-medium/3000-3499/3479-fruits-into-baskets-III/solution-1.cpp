#include <bits/stdc++.h>
using namespace std;

// super hard question
// note: the intuitive solution is brute force, which is O(n^2), passed 736/740 test cases

class Solution
{
public:
    int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets)
    {
        // square root decomposition

        int n = baskets.size();
        int m = sqrt(n);
        int ans = 0;
        int section = (n + m - 1) / m; // basicall ceiling
        vector<int> maxV(section);

        for (int i = 0; i < n; ++i)
        {
            maxV[i / m] = max(maxV[i / m], baskets[i]);
        }

        for (int fruit : fruits)
        {
            int unset = 1;
            int block = 0;
            for (; block < section; ++block)
            {
                if (maxV[block] < fruit)
                    continue;

                int choose = 0;
                maxV[block] = 0;
                for (int i = 0; i < m; ++i)
                {
                    int pos = block * m + i;
                    if (pos < n && baskets[pos] >= fruit && !choose)
                    {
                        baskets[pos] = 0;
                        choose = 1;
                    }
                    if (pos < n)
                    {
                        maxV[block] = max(maxV[block], baskets[pos]);
                    }
                }
                unset = 0;
                break; // this fruit is finished
            }
            ans += unset;
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> fruits = {4, 2, 5};
    vector<int> baskets = {3, 5, 4};
    int result = sol.numOfUnplacedFruits(fruits, baskets);
    cout << "Number of unplaced fruits: " << result << endl; // expected output: 1
    return 0;
}