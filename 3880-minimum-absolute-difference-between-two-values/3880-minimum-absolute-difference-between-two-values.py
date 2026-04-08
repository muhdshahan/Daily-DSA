class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 1 not in nums or 2 not in nums:
            return -1
        min_diff = len(nums)
        for i in range(len(nums)):
            if nums[i]==1:
                for j in range(len(nums)):
                    if i!=j and nums[j]==2:
                        if abs(i-j)<min_diff:
                            min_diff=abs(i-j)
        return min_diff
        # new_dic = {}
        # for i in range(len(nums)):
        #     if nums[i] in [1,2]:
        #         if nums[i] in new_dic:
        #             new_dic[nums[i]].append(i)
        #         else:
        #             new_dic[nums[i]]=[i]
        # print(new_dic)
        # first = abs(min(new_dic[1])-min(new_dic[2]))
        # second = abs(max(new_dic[1])-min(new_dic[2]))
        # third = abs(max(new_dic[1])-max(new_dic[2]))
        # fourth = abs(min(new_dic[1])-max(new_dic[2]))
        # return min(first,second,third,fourth)