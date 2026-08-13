#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    
        int i = m - 1, j = n - 1, k = m + n - 1; // pointers (nums1, nums2, final arr)

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
            else nums1[k--] = nums2[j--];
        }
        
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}