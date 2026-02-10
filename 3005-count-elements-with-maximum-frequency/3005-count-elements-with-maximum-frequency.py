class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        di = Counter(nums)
        max_freq = max(di.values())
        rslt = 0
        for i in di.values():
            if i == max_freq:
                rslt += i
        return rslt