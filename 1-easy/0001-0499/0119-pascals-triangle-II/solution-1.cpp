#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row = {1};

        for (int i = 1; i < rowIndex + 1; ++i) {
            vector<int> new_row;

            for (int j = 0; j < i + 1; j++) {
                int num = 0;
                if (j == 0 || j == i) num = 1;
                else num = row[j-1] + row[j];

                new_row.push_back(num);
            }

            row = new_row;
        }

        return row;
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}