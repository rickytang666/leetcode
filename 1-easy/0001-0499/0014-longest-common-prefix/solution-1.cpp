#include <bits/stdc++.h>

using namespace std;

class Solution 
{
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        sort(strs.begin(), strs.end());

        string first = strs.front(), last = strs.back();

        int i = 0;

        while (i < first.size() && i < last.size() && first[i] == last[i])
        {
            ++i;
        }

        return (i > 0) ? first.substr(0, i) : "";

    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}