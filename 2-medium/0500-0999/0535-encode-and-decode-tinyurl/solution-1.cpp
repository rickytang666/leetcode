// boring question

#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    unordered_map<string, string> m;
    int i = 0;

    // Encodes a URL to a shortened URL.
    string encode(string longUrl)
    {
        string s = "http://tinyurl.com/" + to_string(i++);
        m[s] = longUrl;
        return s;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl)
    {
        return m[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));

int main()
{
    Solution solution;
    string longUrl = "https://www.example.com/some/long/url";
    string shortUrl = solution.encode(longUrl);
    cout << "Shortened URL: " << shortUrl << endl;
    cout << "Decoded URL: " << solution.decode(shortUrl) << endl;
    cout << "Original URL: " << longUrl << endl;
    return 0;
}