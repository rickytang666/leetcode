#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        // the sets don't have to be ordered (just make sure the nums are unique)
        // use range constructor to quickly populate
        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());

        vector<int> ans;
        for (const int& n : s1) {
            if (s2.contains(n)) ans.push_back(n);
        }

        return ans;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}