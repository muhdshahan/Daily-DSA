class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid_index = len(nums)//2
        middle = nums[mid_index]
        if middle in nums[:mid_index] + nums[mid_index+1:]:
            return False
        return True