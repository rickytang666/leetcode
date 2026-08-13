#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int evalRPN(vector<string> &v)
    {
        int a = 0, b = 0;
        stack<int> st; // only numbers can enter this container

        for (int i = 0; i < v.size(); ++i)
        {
            string s = v[i];

            if (!(s == "+" || s == "-" || s == "*" || s == "/"))
            {
                st.push(stoi(s));
            }
            else
            {
                if (st.size() < 2)
                    return 0;

                b = st.top();
                st.pop();
                a = st.top();
                st.pop();

                int num = 0;

                if (s == "+")
                    num = a + b;
                else if (s == "-")
                    num = a - b;
                else if (s == "*")
                    num = a * b;
                else if (s == "/")
                    num = a / b;

                st.push(num);
            }
        }

        return st.top();
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}