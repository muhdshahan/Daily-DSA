class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        i = 0
        j = 0
        count = 0
        while i<len(fruits):
            if j>=len(baskets):
                i+=1
                j=0
                count+=1
                continue
            if baskets[j]<fruits[i]:
                j+=1
            else:
                baskets[j]=0
                j = 0
                i+=1
                continue
        return count