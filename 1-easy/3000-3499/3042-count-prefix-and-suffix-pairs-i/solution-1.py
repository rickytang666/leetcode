from collections import defaultdict
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)
        ans = 0
        for w in words:
            n = len(w)
            for l in range(1, n + 1):
                if w[:l] == w[n - l:]: ans += freq[w[:l]]
            freq[w] += 1
        return ans