class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        num = Counter(num)
        reslt = []
        for key in num:
            if num[key]>1:
                reslt.append(key)
        return reslt