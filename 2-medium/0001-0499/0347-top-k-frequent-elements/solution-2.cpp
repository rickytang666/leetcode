#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> m;
        for (int n : nums)
        {
            m[n]++;
        }
        // using priority_queue (minheap) to keep just k elements (better than sorting)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        for (auto p : m)
        {
            int num = p.first, freq = p.second;
            minHeap.emplace(freq, num);
            // remove filler elements (keep k)
            if (minHeap.size() > k)
                minHeap.pop();
        }
        vector<int> ans;
        // keep popping since we can't iterate
        while (!minHeap.empty())
        {
            ans.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;
    vector<int> result = sol.topKFrequent(nums, k);
    for (int num : result)
    {
        cout << num << " ";
    }
    cout << endl;
    // Expected output: 1 2 (or 2 1, order doesn't matter
    return 0;
}