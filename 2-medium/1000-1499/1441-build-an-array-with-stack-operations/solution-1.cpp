#include <bits/stdc++.h>
using namespace std;

// 0 ms, beats 100%

class Solution
{
public:
    vector<string> buildArray(vector<int> &target, int n)
    {
        vector<string> ans;
        vector<int> mine;

        int i = 1;

        while (mine != target)
        {
            if (i <= n)
            {
                mine.push_back(i);
                ans.push_back("Push");
                if (find(target.begin(), target.end(), i) == target.end())
                {
                    mine.pop_back();
                    ans.push_back("Pop");
                }
                ++i;
            }
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> target = {1, 3};
    int n = 3;
    auto ans = sol.buildArray(target, n);

    for (auto p : ans)
    {
        cout << p << " ";
    }
    cout << endl;

    return 0;
}