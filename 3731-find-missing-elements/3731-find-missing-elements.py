class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        return [i for i in range(mini,maxi) if i not in nums]