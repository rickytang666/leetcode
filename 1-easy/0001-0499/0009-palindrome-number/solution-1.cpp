#include <bits/stdc++.h>

using namespace std;

class Solution 
{
public:
    bool isPalindrome(int x) 
    {

        if (x < 0) 
        {
            return false;
        }
    
        long long reversed = 0;
        long long original = x;
        
        while (x != 0) 
        {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        
        return original == reversed;

    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}