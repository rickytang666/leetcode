#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int n = s.size(), ans = 0;
        for (int i = n - 1; i >= 0; --i) {
            int num = s[i] - 'A' + 1;
            ans += num * pow(26, n - i - 1);
        }
        return ans;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}