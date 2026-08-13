#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        int curr_len = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != ' ') curr_len++;
            else {
                if (curr_len != 0) len = curr_len;
                curr_len = 0;
            }
        }
        if (curr_len != 0) len = curr_len;
        return len;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}