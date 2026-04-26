class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        x = str(x)
        return False if n[0]==x or x not in n else True