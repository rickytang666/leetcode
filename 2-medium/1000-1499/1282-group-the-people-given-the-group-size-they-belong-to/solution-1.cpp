#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> groupThePeople(vector<int> &groupSizes)
    {
        unordered_map<int, vector<int>> m;
        vector<vector<int>> ans;
        for (int i = 0; i < groupSizes.size(); ++i)
        {
            int size = groupSizes[i];
            m[size].push_back(i);

            if (m[size].size() >= size)
            {
                ans.push_back(m[size]);
                m[size].clear();
            }
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> groupSizes = {3, 3, 3, 3, 3, 1, 3};
    vector<vector<int>> result = sol.groupThePeople(groupSizes);
    for (const auto &group : result)
    {
        cout << "[";
        for (int i = 0; i < group.size(); ++i)
        {
            cout << group[i];
            if (i < group.size() - 1)
                cout << ", ";
        }
        cout << "]\n";
    }
    // Example output: [[0,1,2],[3,4,5],[6]]
    return 0;
}