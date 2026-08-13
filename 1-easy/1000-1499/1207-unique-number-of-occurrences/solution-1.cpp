#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        if (arr.size() == 1)
            return true;

        unordered_map<int, int> m;

        for (int num : arr)
            m[num]++;

        unordered_set<int> s;

        for (auto p : m)
        {
            int cnt = p.second;

            if (s.contains(cnt))
                return false;
            else
                s.insert(cnt);
        }

        return true;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}