#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSum(vector<int>& v) {
        set<int, greater<int>> s;
        for (int n : v) s.insert(n);
        if (*s.begin() < 0) return *s.begin();
        int sum = 0;
        for (int n : s) {
            if (n < 0) break;
            sum += n;
        }
        return sum;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}