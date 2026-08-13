#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string clearDigits(string s) {

        vector<char> stack;

        for(char c : s)
        {
            if (isdigit(c) && !stack.empty()) stack.pop_back();
            
            else stack.push_back(c);
        }

        return string(stack.begin(), stack.end());
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}