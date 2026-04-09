class Solution:
    def countCommas(self, n: int) -> int:
        n = str(n)
        if len(n)<4:
            return 0
        if len(n)<7:
            return int(n)-999
        if len(n)<10:
            return (int(n)-999999)*2 + 999000
        if len(n)<13:
            return (int(n)-999999999)*3 + 999000000*2 + 999000
        if len(n)<16:
            return (int(n)-999999999999)*4 + 999000000000*3 + 999000000*2 + 999000
        if len(n)<19:
            return (int(n)-999999999999999)*5 + 999000000000000*4 + 999000000000*3 + 999000000*2 + 999000