#include <bits/stdc++.h>
using namespace std;

// dumb method - 265 ms 😭

class Solution
{
public:
    int evalRPN(vector<string> &v)
    {
        int i = 0, num = 0;
        while (i < v.size())
        {
            if (i < 2)
            {
                num = stoi(v[i]);
                ++i;
                continue;
            }

            int a = stoi(v[i - 2]), b = stoi(v[i - 1]);

            if (v[i] == "+")
            {
                num = a + b;
            }
            else if (v[i] == "-")
            {
                num = a - b;
            }
            else if (v[i] == "*")
            {
                num = a * b;
            }
            else if (v[i] == "/")
            {
                num = a / b;
            }
            else
            {
                ++i;
                continue;
            }

            v[i] = to_string(num);
            v.erase(v.begin() + i - 2, v.begin() + i);
            --i;
        }

        return num;
    }
};

int main()
{
    Solution sol;
    vector<string> v = {"4", "13", "5", "/", "+"};
    cout << sol.evalRPN(v) << endl; // expected output: 9
    return 0;
}