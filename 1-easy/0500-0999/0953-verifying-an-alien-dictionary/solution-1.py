from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j = 0

            while j < len(w1) and j < len(w2):
                if rank[w1[j]] < rank[w2[j]]:
                    break
                elif rank[w1[j]] > rank[w2[j]]:
                    return False
                j += 1

            if j == min(len(w1), len(w2)) and len(w1) > len(w2):
                return False

        return True