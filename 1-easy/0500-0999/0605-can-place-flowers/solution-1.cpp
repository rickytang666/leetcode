#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        int total = flowerbed.size(), cnt = 0, i = 0;

        while (i < total)
        {
            if (!flowerbed[i])
            {
                if (i > 0 && flowerbed[i - 1])
                {
                    ++i;
                    continue;
                }

                if (i < total - 1 && flowerbed[i + 1])
                {
                    i += 3;
                    continue;
                }

                flowerbed[i] = 1;
                ++cnt;
                i += 2;

                if (cnt >= n)
                    return true;
            }
            else
            {
                i += 2;
            }
        }

        return cnt >= n;
    }
};

int main()
{
    cout << "Hello C++" << endl;
    return 0;
}