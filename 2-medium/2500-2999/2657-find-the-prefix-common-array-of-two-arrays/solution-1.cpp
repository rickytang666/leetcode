#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> findThePrefixCommonArray(vector<int> &A, vector<int> &B)
    {
        int n = A.size();
        vector<int> C(n, 0);
        unordered_map<int, int> m;
        for (int i = 0; i < n; ++i)
        {
            m[A[i]]++;
            m[B[i]]++;
            int cnt = 0;
            for (auto p : m)
            {
                if (p.second > 1)
                    ++cnt;
            }
            C[i] = cnt;
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