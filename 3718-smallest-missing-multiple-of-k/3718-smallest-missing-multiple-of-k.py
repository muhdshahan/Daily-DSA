class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(k,202,k):
            if i not in nums:
                return i