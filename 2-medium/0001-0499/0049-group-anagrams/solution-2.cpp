#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    // Identify an anagram using char frequency signature (without actually sorting the string)

    string getSignature(string s)
    {
        map<char, int> m;
        for (char c : s)
            m[c]++;

        string ans;
        for (auto p : m)
        {
            ans += p.first;
            ans += to_string(p.second);
        }

        return ans;
    }

    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> m;

        for (string s : strs)
        {
            m[getSignature(s)].push_back(s);
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