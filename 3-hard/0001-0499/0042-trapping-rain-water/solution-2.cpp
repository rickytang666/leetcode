#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &v)
    {
        int ans = 0;
        stack<int> st;
        for (int right = 0; right < v.size(); ++right)
        {
            while (!st.empty() && v[st.top()] < v[right])
            {
                int mid = st.top();
                st.pop();
                if (st.empty())
                    break; // no gap
                int left = st.top();
                ans += (min(v[left], v[right]) - v[mid]) * (right - left - 1);
            }
            st.push(right);
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> v = {6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3};
    cout << sol.trap(v) << endl; // expected: 83
    return 0;
}