#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> rearrangeArray(vector<int> &v)
    {
        vector<int> pos, neg, ans;
        for (auto p : v)
        {
            if (p > 0)
                pos.push_back(p);
            else
                neg.push_back(p);
        }

        for (int i = 0; i < pos.size(); ++i)
        {
            ans.push_back(pos[i]);
            ans.push_back(neg[i]);
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {3, 1, -2, -5, 2, -4};
    vector<int> ans = sol.rearrangeArray(v);
    for (auto p : ans)
        cout << p << " ";
    cout << endl; // expected output: [3, -2, 1, -5, 2, -4]
    return 0;
}