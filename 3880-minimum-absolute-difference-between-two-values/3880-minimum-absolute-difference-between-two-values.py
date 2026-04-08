class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 1 not in nums or 2 not in nums:
            return -1
        min_diff = len(nums)
        for i in range(len(nums)):
            if nums[i]==1:
                for j in range(len(nums)):
                    if i!=j and nums[j]==2:
                        if abs(i-j)<min_diff:
                            min_diff=abs(i-j)
                            print(min_diff)
        return min_diff