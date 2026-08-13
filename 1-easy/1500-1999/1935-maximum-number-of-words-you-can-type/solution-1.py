class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenSet = set(brokenLetters)
        def check(word):
            for c in word:
                if c in brokenSet: return False
            return True
        words = text.split(' ')
        return sum(check(word) for word in words)