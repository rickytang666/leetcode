#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int p = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j]) {
                    p += 4;
                    // check left
                    if (j > 0 && grid[i][j-1]) p -= 2;
                    // check up
                    if (i > 0 && grid[i-1][j]) p -= 2;
                }
            }
        }

        return p;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}