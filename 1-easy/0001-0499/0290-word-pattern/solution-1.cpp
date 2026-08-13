#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<string> split_str(string s)
    {
        stringstream ss(s);
        vector<string> v;
        while (getline(ss, s, ' '))
        {
            v.push_back(s);
        }
        return v;
    }

    bool wordPattern(string pattern, string s)
    {
        vector<string> v = split_str(s);
        if (pattern.size() != v.size())
            return false;

        unordered_map<char, string> m1;
        unordered_map<string, char> m2;

        for (int i = 0; i < pattern.size(); ++i)
        {
            if (!m1.contains(pattern[i]) && !m2.contains(v[i]))
            {
                m1.emplace(pattern[i], v[i]);
                m2.emplace(v[i], pattern[i]);
            }
            else
            {
                if (m1.contains(pattern[i]) && m1[pattern[i]] != v[i])
                    return false;
                if (m2.contains(v[i]) && m2[v[i]] != pattern[i])
                    return false;
            }
        }

        return true;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}