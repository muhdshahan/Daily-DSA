class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        asce = sorted(nums)
        desc = asce[::-1]
        lar = sum(desc[:k])
        sma = sum(asce[:k])
        return lar - sma