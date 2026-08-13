from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def getSignature(word):
            return "".join(sorted(word))
        ans = [words[0]]
        for i in range(1, len(words)):
            if getSignature(words[i]) != getSignature(words[i - 1]):
                ans.append(words[i])
        return ans  