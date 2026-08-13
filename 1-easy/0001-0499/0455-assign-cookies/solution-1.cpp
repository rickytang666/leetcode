#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int cnt = 0;
        int i = 0, j = 0;
        while (i < g.size() && j < s.size()) {
            if (g[i] <= s[j++]) {
                ++cnt;
                ++i;
            }
        }
        return cnt;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}