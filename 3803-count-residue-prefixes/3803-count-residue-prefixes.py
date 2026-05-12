class Solution:
    def residuePrefixes(self, s: str) -> int:
        rslt = 0
        for win_len in range(len(s)):
            prefix = s[:win_len+1]
            distinct_char = set(prefix)
            if len(distinct_char)==len(prefix)%3:
                rslt += 1
        return rslt