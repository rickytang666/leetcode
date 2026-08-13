#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        if (position.size() == 1)
            return 1;

        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); ++i)
        {
            cars.emplace_back(position[i], speed[i]);
        }
        sort(cars.begin(), cars.end());
        stack<double> times;
        for (auto p : cars)
        {
            times.push(double(target - p.first) / p.second);
        }

        int ans = 1;

        while (times.size() > 1)
        {
            double lead = times.top();
            times.pop();
            if (lead < times.top())
            {
                ++ans;
            }
            else
            {
                times.top() = lead;
            }
        }

        return ans;
    }
};

int main()
{
    int target = 10;
    vector<int> position = {0, 4, 2}, speed = {2, 1, 3};
    Solution sol;
    cout << sol.carFleet(target, position, speed) << endl;
    return 0;
}