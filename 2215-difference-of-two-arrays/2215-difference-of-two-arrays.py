class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        rslt = []
        for i in nums1:
            if i not in nums2:
                rslt.append(i)
        r = []
        for i in nums2:
            if i not in nums1:
                r.append(i)
        return [list(set(rslt)), list(set(r))]