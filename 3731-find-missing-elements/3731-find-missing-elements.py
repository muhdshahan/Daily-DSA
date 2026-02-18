class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        mini = min(nums)
        maxi = max(nums)
        rslt = []
        for i in range(mini,maxi):
            print(i)
            if i not in nums:
                rslt.append(i)
        return rslt