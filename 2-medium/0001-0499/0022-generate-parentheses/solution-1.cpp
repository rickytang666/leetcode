#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<string> generateParenthesis(int n)
    {
        vector<string> ans;
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    void backtrack(vector<string> &ans, string current, int open_cnt, int close_cnt, int n)
    {
        /*
        Ensure:
        neither open_cnt or close_cnt exceed n,
        close_cnt < open_cnt at any point before finish
        */

        if (open_cnt == n && close_cnt == n)
        {
            ans.push_back(current);
            return;
        }

        if (open_cnt < n)
        {
            backtrack(ans, current + "(", open_cnt + 1, close_cnt, n);
        }

        if (close_cnt < open_cnt)
        {
            backtrack(ans, current + ")", open_cnt, close_cnt + 1, n);
        }
    }
};

int main()
{
    Solution sol;
    int n = 3;
    vector<string> result = sol.generateParenthesis(n);
    for (const string &s : result)
    {
        cout << s << endl;
    }
    // expected output: "((()))", "(()())", "(())()", "()(())", "()()()"
    return 0;
}