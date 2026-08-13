#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool closeStrings(string word1, string word2)
    {
        int n1 = word1.size(), n2 = word2.size();

        if (n1 != n2)
            return false;

        vector<int> v1(26, 0), v2(26, 0);

        for (int i = 0; i < n1; ++i)
        {
            v1[word1[i] - 'a']++;
            v2[word2[i] - 'a']++;
        }

        // two words must have same kinds of letters

        for (int i = 0; i < 26; ++i)
        {
            if (v1[i] == 0 && v2[i] != 0)
                return false;
            if (v2[i] == 0 && v1[i] != 0)
                return false;
        }

        // combinations of frequencies must be same as well

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());

        return v1 == v2;
    }
};

int main()
{
    Solution sol;
    string word1 = "xxxxxxxxxxxxxxxxxxx", word2 = "zzzzzzzzzzzzzzzzzzz";
    cout << sol.closeStrings(word1, word2) << endl;
    return 0;
}