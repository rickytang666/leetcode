#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> findThePrefixCommonArray(vector<int> &A, vector<int> &B)
    {
        int n = A.size();
        vector<int> C(n, 0);
        vector<int> freq(n + 1, 0); // make the index able to reach n
        int common = 0;
        for (int i = 0; i < n; ++i)
        {
            if (++freq[A[i]] > 1)
                ++common;
            if (++freq[B[i]] > 1)
                ++common;
            C[i] = common;
        }
        return C;
    }
};

int main()
{
    Solution sol;
    vector<int> A = {1, 3, 2, 4};
    vector<int> B = {3, 1, 2, 4};
    vector<int> result = sol.findThePrefixCommonArray(A, B);
    for (int x : result)
    {
        cout << x << " ";
    }
    cout << endl;
    // Expected output: 0 1 2 3
    return 0;
}