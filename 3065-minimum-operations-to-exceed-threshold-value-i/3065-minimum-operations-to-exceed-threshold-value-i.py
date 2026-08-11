class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num = [x for x in nums if x < k]
        return len(num)