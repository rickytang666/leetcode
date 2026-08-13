#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {

        unordered_map<char, int> letters;

        for (char ch : magazine)
        {
            letters[ch]++;
        }

        for (char ch : ransomNote)
        {
            if (!letters[ch])
            {
                return false;
            }

            letters[ch]--;
        }

        return true;
        
    }
};

int main() {
    cout << "Hello C++" << endl;
    return 0;
}