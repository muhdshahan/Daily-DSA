class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        dicti = Counter(nums)
        for j in dicti:
            if j>nums[0] and dicti[j]!=dicti[nums[0]]:
                return [nums[0],j]
        return [-1,-1]

            