#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets)
    {
        int n = fruits.size();
        int ans = n;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (baskets[j] >= fruits[i])
                {
                    baskets[j] = 0;
                    ans--;
                    break;
                }
            }
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
    cout << "Number of unplaced fruits: " << result << endl; // expected output: 0
    return 0;
}