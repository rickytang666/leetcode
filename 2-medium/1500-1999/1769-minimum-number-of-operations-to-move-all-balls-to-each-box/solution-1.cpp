#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> minOperations(string boxes)
    {
        int n = static_cast<int>(boxes.length());

        vector<int> v(n, 0);
        for (int i = 0; i < n; ++i)
        {
            int cnt = 0;
            for (int j = i - 1; j >= 0; --j)
            {
                if (boxes[j] != '0')
                    cnt += abs(i - j);
            }
            for (int k = i + 1; k < n; ++k)
            {
                if (boxes[k] != '0')
                    cnt += abs(i - k);
            }
            v[i] = cnt;
        }

        return v;
    }
};

int main()
{
    Solution sol;
    string boxes = "110";
    vector<int> result = sol.minOperations(boxes);
    for (int ops : result)
    {
        cout << ops << " ";
    }
    cout << endl;
    // Expected output: 1 1 3
    return 0;
}