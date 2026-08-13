class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def val(word):
            arr = []
            for c in word:
                arr.append(str(ord(c) - ord('a')))
            return int(''.join(arr))
        return val(firstWord) + val(secondWord) == val(targetWord)