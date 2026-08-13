#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // Gaussian summation method
        int n = nums.size();
        int expected_sum = n * (n + 1)/2;
        int actual_sum = accumulate(nums.begin(), nums.end(), 0);
        return expected_sum - actual_sum;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}