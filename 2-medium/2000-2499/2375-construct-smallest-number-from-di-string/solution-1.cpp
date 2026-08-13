#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string smallestNumber(string pattern)
    {
        stack<int> st;
        string ans;
        for (int i = 0; i <= pattern.size(); ++i)
        {
            st.push(i + 1);

            if (i == pattern.size() || pattern[i] == 'I')
            {
                while (!st.empty())
                {
                    ans += to_string(st.top());
                    st.pop();
                }
            }
        }

        return ans;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}