#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string a, string b) {
        if (a == b) return true;
        
        unordered_map<char, char> m1, m2;
        for (int i = 0; i < a.size(); ++i) {
            if (m1.contains(a[i])) a[i] = m1[a[i]];
            else {
                if (m2.contains(b[i]) && m2[b[i]] != a[i]) {
                    return false; // Conflict in mapping
                }
                if (a[i] == b[i] || !m2.contains(b[i])) {
                    m1.emplace(a[i], b[i]);
                    m2.emplace(b[i], a[i]);
                    a[i] = b[i];
                }
            }
        }

        cout << "m1: " << endl;
        for (const auto& [key, value] : m1) {
            cout << key << " -> " << value << endl;
        }

        cout << "m2: " << endl;
        for (const auto& [key, value] : m2) {
            cout << key << " -> " << value << endl;
        }

        return a == b;
    }
};

int main() {
    Solution sol;
    string s = "egcd", t = "adfd";
    cout << (sol.isIsomorphic(s, t) ? "true" : "false") << endl;
    return 0;
}