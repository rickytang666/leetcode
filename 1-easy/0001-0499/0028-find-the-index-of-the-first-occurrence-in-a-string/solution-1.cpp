#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int strStr(string a, string b) {
        int a_length = a.size();
        int b_length = b.size();
        if (a_length < b_length) return -1; // size_t is unsigned
        for (int i = 0; i <= a_length - b_length; ++i) {
            if (a.substr(i, b_length) == b) return i;
        }
        return -1;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}