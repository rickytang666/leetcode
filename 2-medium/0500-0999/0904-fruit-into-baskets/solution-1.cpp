#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    // expand the window by moving the end and adding fruits
    // if the map has more than 2 types, shrink the start of the window until desired

    int totalFruit(vector<int> &fruits)
    {
        int ans = 0, start = 0;
        unordered_map<int, int> basket;

        for (int end = 0; end < fruits.size(); ++end)
        {
            basket[fruits[end]]++;

            while (basket.size() > 2)
            {
                basket[fruits[start]]--;
                if (basket[fruits[start]] == 0)
                {
                    basket.erase(fruits[start]);
                }
                start++;
            }

            ans = max(ans, end - start + 1);
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> fruits = {1, 2, 1};
    cout << sol.totalFruit(fruits) << endl; // expected output: 3
    return 0;
}