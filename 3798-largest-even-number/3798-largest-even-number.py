class Solution:
    def largestEven(self, s: str) -> str:
        tr_len = 0
        for i in s[::-1]:
            if i=='1':
                tr_len+=1
            else:
                return s[:len(s)-tr_len]
        return s[:len(s)-tr_len]