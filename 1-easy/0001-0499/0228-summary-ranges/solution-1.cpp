#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;

        if (nums.empty()) {
            return ans;
        }

        int start = 0, end = 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i-1] + 1) {
                end = i - 1;
                string s = (start == end)
                               ? to_string(nums[start])
                               : format("{}->{}", nums[start], nums[end]);
                start = i;
                end = i;
                ans.push_back(s);
            } else {
                end = i;
            }
        }
        
        // finish up the last range
        string s = (start == end)
                               ? to_string(nums[start])
                               : format("{}->{}", nums[start], nums[end]);
        ans.push_back(s);
        return ans;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}