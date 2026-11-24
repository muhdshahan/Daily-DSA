class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        rslt = 0
        if nums[0]>=nums[1]:
            rslt+=1
        if nums[-1]>=nums[-2]:
            rslt+=1
        if len(nums)==2:
            return rslt
        for i in range(len(nums)-2):
            avg = (nums[i] + nums[i+2])/2
            if nums[i+1]>=avg:
                rslt += 1
        return rslt