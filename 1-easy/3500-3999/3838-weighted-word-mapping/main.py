from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for w in words:
            tmp = sum(weights[ord(c) - ord('a')] for c in w) % 26
            ans.append(chr(ord('z') - tmp))
        return ''.join(ans)