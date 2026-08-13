#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string largestGoodInteger(string num)
    {
        int max = -1;
        string ans = "";
        for (int i = 0; i < num.size() - 2; ++i)
        {
            if (num[i] == num[i + 1] && num[i + 1] == num[i + 2])
            {
                int x = num[i] - 1;
                if (x > max)
                {
                    ans = string(3, num[i]);
                    if (x == 9)
                        return ans;
                    max = x;
                }
            }
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    string num = "6777133339";
    cout << sol.largestGoodInteger(num) << endl; // expected output: "777"
    return 0;
}