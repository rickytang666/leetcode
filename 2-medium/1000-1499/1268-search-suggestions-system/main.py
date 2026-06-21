from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestions = []

    def addSuggestion(self, product):
        if len(self.suggestions) < 3:
            self.suggestions.append(product)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()

        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.addSuggestion(p)
        
        ans, node = [], root
        for char in searchWord:
            node = node.children[char]
            ans.append(node.suggestions)
        
        return ans