#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int compress(vector<char> &chars)
    {
        if (chars.size() == 1)
            return 1;

        int len = 1;
        vector<char> ans;

        for (int i = 1; i < chars.size(); ++i)
        {
            if (chars[i] == chars[i - 1])
            {
                ++len;
            }
            else
            {
                ans.push_back(chars[i - 1]);
                if (len > 1)
                {
                    string s = to_string(len);
                    for (char c : s)
                    {
                        ans.push_back(c);
                    }
                    len = 1;
                }
            }
        }

        ans.push_back(chars.back());

        if (len > 1)
        {
            string s = to_string(len);
            for (char c : s)
            {
                ans.push_back(c);
            }
            len = 1;
        }

        chars = ans;
        return chars.size();
    }
};

int main()
{
    Solution sol;
    vector<char> chars = {'a', 'a', 'b', 'b', 'c', 'c', 'c'};
    int newLength = sol.compress(chars);
    cout << "Compressed length: " << newLength << endl;
    cout << "Compressed characters: ";
    for (char c : chars)
    {
        cout << c;
    }
    cout << endl;
    // expected output: Compressed length: 6, Compressed characters: a2b2c3
    return 0;
}