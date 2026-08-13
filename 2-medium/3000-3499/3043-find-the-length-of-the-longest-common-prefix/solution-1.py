from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, num):
        node = self.root
        for d in num:
            if d not in node.children: node.children[d] = TrieNode()
            node = node.children[d]
    def longest_prefix(self, num):
        node = self.root
        ans = 0
        for d in num:
            if d not in node.children: break
            node = node.children[d]
            ans += 1
        return ans

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        for x in arr1: t.insert(str(x))
        ans = 0
        for y in arr2: ans = max(ans, t.longest_prefix(str(y)))
        return ans