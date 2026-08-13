#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& v) {
        int maximum = 0;
        int cnt = 0;
        for (int i = 0; i < v.size(); ++i) {
            if (v[i]) ++cnt;
            else {
                maximum = max(maximum, cnt);
                cnt = 0;
            }
        }

        maximum = max(maximum, cnt);

        return maximum;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}