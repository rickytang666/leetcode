#include <bits/stdc++.h>
using namespace std;

class MinStack
{
public:
    MinStack()
    {
        // don't need to do anything
    }

    void push(int val)
    {
        st.push(val);
        if (min_st.empty())
        {
            min_st.push(val);
        }
        else if (min_st.top() >= val)
        {
            min_st.push(val);
        }
    }

    void pop()
    {
        if (st.top() == min_st.top())
        {
            min_st.pop();
        }
        st.pop();
    }

    int top()
    {
        return st.top();
    }

    int getMin()
    {
        return min_st.top();
    }

private:
    stack<int> st, min_st;
};

int main()
{
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    cout << minStack.getMin() << endl; // expected output: -3
    minStack.pop();
    cout << minStack.top() << endl;    // expected output: 0
    cout << minStack.getMin() << endl; // expected output: -2
    return 0;
}