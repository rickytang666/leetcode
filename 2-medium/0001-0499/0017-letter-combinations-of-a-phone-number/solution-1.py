from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n = len(digits)
        ans = []

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, path):
            if i == n:
                ans.append(path)
                return

            letters = m[digits[i]]
            for letter in letters:
                backtrack(i + 1, path + letter)

        backtrack(0, "")
        return ans
            