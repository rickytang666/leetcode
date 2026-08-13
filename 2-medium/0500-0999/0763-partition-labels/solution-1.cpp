#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> partitionLabels(string s)
    {
        int n = s.size();
        vector<int> last(26, -1);

        for (int i = 0; i < n; ++i)
        {
            last[s[i] - 'a'] = i;
        }

        vector<int> ans;
        int start = 0, end = 0;

        for (int i = 0; i < n; ++i)
        {
            end = max(end, last[s[i] - 'a']);
            if (i == end)
            {
                ans.push_back(end - start + 1);
                start = i + 1;
            }
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    string s = "ababcbacadefegdehijhklij";
    vector<int> result = sol.partitionLabels(s);
    for (int len : result)
    {
        cout << len << " ";
    }
    cout << endl; // expected output: 9 7 8
    return 0;
}