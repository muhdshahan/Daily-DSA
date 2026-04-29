class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            rem = nums[i+1:]
            if nums[i] > sum(rem)/len(rem):
                count+=1
        return count