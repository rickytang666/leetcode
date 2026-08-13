#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& a, vector<int>& b) {
        unordered_map<int, int> m;
        for (const int& n : a) ++m[n];
        vector<int> ans;
        // ans doesn't have to be sorted
        for (const int& n : b) {
            if (m[n]-- > 0) ans.push_back(n);
        }
        return ans;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}