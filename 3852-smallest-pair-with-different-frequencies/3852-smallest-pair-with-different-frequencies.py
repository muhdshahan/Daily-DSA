class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        tot_pairs = [sum(nums)]
        dicti = Counter(nums)
        for j in dicti:
            pair = [nums[0]]
            if j>nums[0] and dicti[j]!=dicti[nums[0]]:
                pair.append(j)
                return pair
        return [-1,-1]

            