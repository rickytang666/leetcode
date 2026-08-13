#include <bits/stdc++.h>

using namespace std;

class NumArray {
public:
    NumArray(vector<int>& nums) {
        arr.push_back(0);
        for (int n : nums) {
            arr.push_back(arr.back() + n);
        }
    }
    
    int sumRange(int left, int right) {
        return arr[right + 1] - arr[left];
    }
private:
    vector<int> arr;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */

int main() {
    cout << "Hello C++" << endl;
    return 0;
}