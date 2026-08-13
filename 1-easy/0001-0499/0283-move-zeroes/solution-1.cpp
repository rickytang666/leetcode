#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // since non-zero elements are always ahead of zeros, move the non-zeros ahead
        int j = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) nums[j++] = nums[i];
        }
        for (; j < nums.size(); ++j) {
            nums[j] = 0;
        }
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}