#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        vector<vector<int>> rows(9, vector<int>(9, 0)), cols(9, vector<int>(9, 0)), boxes(9, vector<int>(9, 0));

        for (int i = 0; i < 9; ++i)
        {
            for (int j = 0; j < 9; ++j)
            {
                char c = board[i][j];
                if (c == '.')
                    continue;

                int num = c - '1'; // map to 0-8
                int box_index = (i / 3) * 3 + j / 3;
                if (rows[i][num] || cols[j][num] || boxes[box_index][num])
                    return false;
                rows[i][num] = cols[j][num] = boxes[box_index][num] = 1;
            }
        }

        return true;
    }
};

int main()
{
    Solution sol;
    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '6', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
    bool result = sol.isValidSudoku(board);
    cout << (result ? "Valid Sudoku" : "Invalid Sudoku") << endl;
    // example output: Valid Sudoku
    return 0;
}