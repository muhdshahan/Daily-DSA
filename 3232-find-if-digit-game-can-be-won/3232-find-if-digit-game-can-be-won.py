class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        for n in nums:
            if len(str(n))==1:
                single_sum+= n
            else:
                double_sum+= n
        return False if single_sum == double_sum else True