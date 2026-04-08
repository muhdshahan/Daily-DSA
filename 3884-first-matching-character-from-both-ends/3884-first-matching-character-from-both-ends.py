class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for i in range(len(s)):
            if s[i]==s[len(s)-i-1]:
                return i
            if i>=len(s)-i-1:
                return -1