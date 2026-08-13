#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int len = nums.size();
        
        int tuples_count = 0;

        vector<int> pair_products;

        for (int i = 0; i < len; ++i)
        {
            for (int j = i + 1; j < len; ++j)
            {
                pair_products.push_back(nums[i] * nums[j]);
            }
        }

        sort(pair_products.begin(), pair_products.end());

        int last_product = -1, same_product_count = 0;

        for (int i = 0; i < pair_products.size(); ++i)
        {
            if (pair_products[i] == last_product)
            {
                same_product_count++;
            }
            else
            {
                int pairs = same_product_count * (same_product_count - 1)/2;
                tuples_count += 8 * pairs;
                last_product = pair_products[i];
                same_product_count = 1;
            }
        }

        int pairs = same_product_count * (same_product_count - 1)/2;
        tuples_count += 8 * pairs;

        return tuples_count;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}