class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                # python slicing syntax
                return word[i::-1] + word[i+1:]
        return word
    
print(Solution().reversePrefix("abcdefd", 'd')) # expected output: dcbaefd