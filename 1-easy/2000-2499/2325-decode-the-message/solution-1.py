class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {' ' : ' '}
        ans = []
        i = 0
        for ch in key:
            if ch not in mp:
                mp[ch] = chr(i + ord('a'))
                i += 1
        for ch in message:
            ans.append(mp[ch])
        return ''.join(ans)