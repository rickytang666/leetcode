#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int, greater<int>> s;
        for (const int& n : nums) {
            s.insert(n);
        }
        auto it = s.begin();
        if (s.size() < 3) return *it;
        else {
            advance(it, 2);
            return *it;
        }
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}