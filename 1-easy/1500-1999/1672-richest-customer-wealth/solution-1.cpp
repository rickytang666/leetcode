#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        
        int max_val = 0;

        for (auto& customer : accounts)
        {
            max_val = max(max_val, accumulate(customer.begin(), customer.end(), 0));
        }

        return max_val;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}