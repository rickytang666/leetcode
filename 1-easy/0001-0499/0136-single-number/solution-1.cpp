#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i = 0;
        while (i < nums.size() - 1) {
            if (nums[i + 1] != nums[i]) {
                break;
            } else i += 2;
        }

        return nums[i];
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}