class Solution:
    def countCommas(self, n: int) -> int:
        n = str(n)
        if len(n)<4:
            return 0
        if len(n)>=4 and len(n)<7:
            return int(n)-999