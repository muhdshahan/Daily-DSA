class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        tot_pairs = [sum(nums)]
        dicti = Counter(nums)
        for j in dicti:
            pair = [nums[0]]
            if j>nums[0] and dicti[j]!=dicti[nums[0]]:
                pair.append(j)
                if sum(tot_pairs)>sum(pair):
                    tot_pairs=pair
        return [-1,-1] if len(tot_pairs)<2 else tot_pairs

            