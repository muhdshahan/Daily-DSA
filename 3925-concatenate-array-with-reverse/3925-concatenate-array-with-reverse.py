class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums_rev = nums[::-1]
        return nums + nums_rev