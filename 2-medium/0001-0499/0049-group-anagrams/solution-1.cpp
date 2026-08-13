#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> m;

        for (string s : strs)
        {
            string key = s;
            sort(key.begin(), key.end());
            m[key].push_back(s);
        }

        for (auto p : m)
        {
            ans.push_back(p.second);
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = sol.groupAnagrams(strs);
    for (const auto &group : result)
    {
        for (const auto &word : group)
        {
            cout << word << " ";
        }
        cout << endl;
    }
    return 0;
}