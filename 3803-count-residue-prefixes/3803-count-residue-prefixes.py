class Solution:
    def residuePrefixes(self, s: str) -> int:
        rslt = 0
        for win_len in range(len(s)):
            if len(set(s[:win_len+1]))==len(s[:win_len+1])%3:
                rslt += 1
        return rslt