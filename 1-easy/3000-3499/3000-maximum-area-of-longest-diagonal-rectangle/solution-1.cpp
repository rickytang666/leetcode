#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int areaOfMaxDiagonal(vector<vector<int>> &dimensions)
    {
        int maxD = 0, maxArea = 0;
        for (auto &rect : dimensions)
        {
            int l = rect[0], w = rect[1];
            int d = pow(l, 2) + pow(w, 2), area = l * w;
            if (d > maxD)
            {
                maxD = d;
                maxArea = area;
            }
            else if (d == maxD)
            {
                maxArea = max(maxArea, area);
            }
        }
        return maxArea;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}