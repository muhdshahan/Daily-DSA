class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        parity = ["even" if nums[i]%2==0 else "odd" for i in range(len(nums))]
        rslt = []
        for i in range(len(parity)-1):
            count = 0
            for j in range(i+1,len(parity)):
                if parity[i]!=parity[j]:
                    count+=1
            rslt.append(count)
        rslt.append(0)
        return rslt