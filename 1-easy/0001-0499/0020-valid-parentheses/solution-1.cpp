#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isOpen (char c) {
        if (c == '(' || c == '[' || c == '{') return true;
        return false;
    }

    bool isValid(string s) {
        map<char, char> bracket_pairs;
        bracket_pairs['('] = ')';
        bracket_pairs['['] = ']';
        bracket_pairs['{'] = '}';

        if (s.size() % 2 == 1) return false;

        stack<char> st;

        for (char c : s) {
            if (isOpen(c)) st.push(c);
            else {
                if (!st.empty() && c == bracket_pairs[st.top()]) st.pop();
                else return false;
            }
        }

        return st.empty();
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}