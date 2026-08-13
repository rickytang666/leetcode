#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string ans = "";

        int i = 0, j = 0;

        auto s1 = word1.size(), s2 = word2.size();

        while (i < s1 || j < s2)
        {
            if (i < s1)
                ans += word1[i++];
            if (j < s2)
                ans += word2[j++];
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    cout << sol.mergeAlternately("abc", "pqr") << endl; // expected: "apbqcr"
    return 0;
}