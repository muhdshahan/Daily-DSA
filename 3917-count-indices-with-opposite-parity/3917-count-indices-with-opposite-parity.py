class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        parity = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                parity.append("even")
            else:
                parity.append("odd")
        rslt = []
        for i in range(len(parity)-1):
            count = 0
            for j in range(i+1,len(parity)):
                if parity[i]!=parity[j]:
                    count+=1
                print(parity[i],parity[j],count)
            rslt.append(count)
        rslt.append(0)
        return rslt