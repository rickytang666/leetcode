#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int current = nums[0];
        int i = 1;
        while (i < nums.size())
        {
            if (nums[i] != current)
            {
                current = nums[i];
                ++i;
            }
            else
            {
                nums.erase(nums.begin() + i);
            }
        }
        
        return nums.size();
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}