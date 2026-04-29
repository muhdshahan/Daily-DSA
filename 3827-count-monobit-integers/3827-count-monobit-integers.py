class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            binary = str(bin(i)[2:])
            print(binary)
            if "0" in binary and "1" in binary:
                continue
            else:
                count+=1
        return count