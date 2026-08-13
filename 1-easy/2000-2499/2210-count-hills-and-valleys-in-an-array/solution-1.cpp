#include <bits/stdc++.h>

using namespace std;

class Solution {
public:

    int countHillValley(vector<int>& nums) {
        int cnt = 0, n = nums.size();
        for (int i = 1; i < n - 1; ++i) {
            if (nums[i] == nums[i-1]) continue;

            int j = i + 1;
            while (nums[j] == nums[i] && j < n - 1) ++j;

            if ((nums[i - 1] > nums[i] && nums[j] > nums[i]) || nums[i - 1] < nums[i] && nums[j] < nums[i]) ++cnt;
        }
        return cnt;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}