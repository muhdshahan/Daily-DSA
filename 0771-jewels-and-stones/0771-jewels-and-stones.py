class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        rslt = 0
        for i in jewels:
            rslt += stones[i]
        return rslt