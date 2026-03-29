class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        value_set = Counter(nums)
        unique = [ key for key in value_set if value_set[key]==1 ]
        for i in range(len(nums)):
            if nums[i]%2==0:
                if nums[i] in unique:
                    return nums[i]
        return -1