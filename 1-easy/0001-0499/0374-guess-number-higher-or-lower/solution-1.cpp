#include <bits/stdc++.h>
using namespace std;

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

int guess(int num);

// Mock implementation of the guess function for testing purposes
int guess(int num)
{
    static int picked = 6; // Let's assume the picked number is 6 for testing
    if (num < picked)
        return 1; // num is lower than the picked number
    else if (num > picked)
        return -1; // num is higher than the picked number
    return 0;      // num is equal to the picked number
}

class Solution
{
public:
    int guessNumber(int n)
    {
        int low = 1, high = n;
        while (low <= high)
        {
            int mid = low + (high - low) / 2;
            int res = guess(mid);
            if (res == 0)
                return mid;
            else if (res == -1)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return -1;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}