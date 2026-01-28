class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_element = max(nums)
        return (len(nums)*max_element) - sum(nums)