#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& v) {
        // iterate through the array and find out all present numbers by assigning negative values to their corresponding slots
        int n = v.size();
        for (int i = 0; i < n; ++i) {
            int num = abs(v[i]);
            int index = num - 1;
            if (v[index] > 0) v[index] *= -1;
        }

        vector<int> ans;
        for (int i = 0; i < n; ++i) {
            // get all the missing numbers (positive slots)
            if (v[i] > 0) ans.push_back(i + 1);
        }
        return ans;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}