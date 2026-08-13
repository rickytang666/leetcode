#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        
        int n = queries.size();
        vector<int> results(n);
        unordered_map<int, int> colors, balls;

        for (int i = 0; i < n; ++i)
        {
            int ball = queries[i][0], color = queries[i][1];

            if (balls.find(ball) != balls.end())
            {
                int prev_col = balls[ball];
                colors[prev_col]--;

                if (colors[prev_col] <= 0) colors.erase(prev_col);
            }

            balls[ball] = color;
            colors[color]++;

            results[i] = colors.size();
        }

        return results;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}