from typing import List

"""
i was hella confused by this question :(
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        t = Trie()
        for w in dictionary:
            t.addWord(w)
        dp = {len(s) : 0}
        def dfs(i):
            if i in dp: return dp[i]
            ans = 1 + dfs(i + 1)
            curr = t.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    ans = min(ans, dfs(j + 1))
            dp[i] = ans
            return ans
        return dfs(0)