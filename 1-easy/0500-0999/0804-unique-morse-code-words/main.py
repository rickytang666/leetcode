from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            res.add(''.join(morse[ord(c) - ord('a')] for c in word))
        return len(res)