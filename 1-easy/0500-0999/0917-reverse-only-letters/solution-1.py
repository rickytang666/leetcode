class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        char_list = list(s)
        while l < r:
            if char_list[l].isalpha() and char_list[r].isalpha():
                char_list[l], char_list[r] = char_list[r], char_list[l]
                r -= 1
                l += 1
            else:
                if not char_list[l].isalpha(): l += 1
                if not char_list[r].isalpha(): r -= 1
        return "".join(char_list)
