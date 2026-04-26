class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)<3:
            return nums
        rslt = [nums[0]]
        for i in range(1,len(nums)-1):
            left_max = max(nums[:i])
            right_max = max(nums[i+1:])
            if left_max and nums[i]>left_max:
                rslt.append(nums[i])
            elif right_max and nums[i]>right_max:
                rslt.append(nums[i])
        rslt.append(nums[-1])
        return rslt