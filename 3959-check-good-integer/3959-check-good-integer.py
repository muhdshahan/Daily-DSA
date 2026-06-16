class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        n = str(n)
        digitSum = 0
        squareSum = 0
        for num in n:
            digitSum += int(num)
            squareSum += int(num) * int(num)
        
        return True if squareSum - digitSum >= 50 else False