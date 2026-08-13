#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0], profit = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] < buy) {
                buy = prices[i];
            } else profit = max(prices[i] - buy, profit);
        }

        return profit;        
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}