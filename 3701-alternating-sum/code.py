class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_sum = sum([ nums[ind] for ind in range(len(nums)) if ind%2==0 ])
        odd_sum = sum([ nums[ind] for ind in range(len(nums)) if ind%2!=0 ])
        return even_sum - odd_sum