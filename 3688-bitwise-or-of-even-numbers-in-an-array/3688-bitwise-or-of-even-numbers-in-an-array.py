class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        rslt = 0
        for i in nums:
            if i%2==0:
                rslt = rslt|i
        return rslt