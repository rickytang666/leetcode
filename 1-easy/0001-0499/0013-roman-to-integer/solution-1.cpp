#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int romanToInt(string s) 
    {
        map<char, int> roman_numerals;

        int answer = 0;
    
        roman_numerals['I'] = 1;
        roman_numerals['V'] = 5;
        roman_numerals['X'] = 10;
        roman_numerals['L'] = 50;
        roman_numerals['C'] = 100;
        roman_numerals['D'] = 500;
        roman_numerals['M'] = 1000;

        for (int i = 0; i < s.size(); ++i)
        {
            answer += roman_numerals[s[i]];

            if (roman_numerals[s[i]] < roman_numerals[s[i + 1]])
            {
                answer -= 2 * roman_numerals[s[i]];
            }

        }

        return answer;

    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}