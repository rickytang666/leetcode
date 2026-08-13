#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxVowels(string str, int k)
    {
        vector<int> v(26, 0);
        v[0] = 1, v[4] = 1, v[8] = 1, v[14] = 1, v[20] = 1;
        int cnt = 0;
        for (int i = 0; i < k; ++i)
        {
            if (v[str[i] - 'a'])
                ++cnt;
        }
        int ans = cnt;
        for (int i = k; i < str.size(); ++i)
        {
            if (v[str[i] - 'a'])
                ++cnt;
            if (v[str[i - k] - 'a'])
                --cnt;
            ans = max(ans, cnt);

            if (ans == k)
                return ans;
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    string s = "abciiidef";
    int k = 3;
    cout << sol.maxVowels(s, k) << endl; // expected output: 3
    return 0;
}