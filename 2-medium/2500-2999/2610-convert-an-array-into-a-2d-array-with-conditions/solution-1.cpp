#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> findMatrix(vector<int> &nums)
    {
        unordered_map<int, int> m;
        for (int n : nums)
            m[n]++;
        vector<vector<int>> v;
        for (auto p : m)
        {
            for (int i = 0; i < p.second; ++i)
            {
                if (v.size() < p.second)
                    v.emplace_back();
                v[i].push_back(p.first);
            }
        }
        return v;
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> test_cases = {
        {1, 3, 4, 1, 2, 3, 1},
        {1, 2, 3, 4}};

    for (auto &test_case : test_cases)
    {
        vector<vector<int>> result = sol.findMatrix(test_case);
        for (const auto &row : result)
        {
            for (int num : row)
            {
                cout << num << " ";
            }
            cout << endl;
        }
        cout << "-----" << endl;
    }

    return 0;
}