#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        int i = 0, j = s.size() - 1;
        while (i < j)
        {
            swap(s[i++], s[j--]);
        }
    }
};

int main()
{
    Solution solution;
    vector<char> s = {'h', 'e', 'l', 'l', 'o'};
    solution.reverseString(s);
    for (char c : s)
    {
        cout << c << " ";
    }
    cout << endl;
    return 0;
}