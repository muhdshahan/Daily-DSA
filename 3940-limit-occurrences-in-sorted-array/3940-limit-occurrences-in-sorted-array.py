class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        rslt = []
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1
            if check[i] <= k:
                rslt.append(i)
                
        return rslt