class Solution:
    def minOperations(self, nums: List[int]) -> int:
        rslt = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                rslt +=1
                for j in range(len(nums[i:i+3])):
                        nums[j+i] = nums[j+i]^1
        if 0 in nums:
            return -1
        return rslt

