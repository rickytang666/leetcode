#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>

using namespace std;

class Solution
{
public:
    vector<string> sortPeople(vector<string> &names, vector<int> &heights)
    {
        map<int, string, greater<int>> mp;
        for (int i = 0; i < names.size(); ++i)
        {
            mp[heights[i]] = names[i];
        }
        vector<string> ans;
        for (auto &p : mp)
            ans.push_back(p.second);
        return ans;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}