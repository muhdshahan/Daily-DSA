class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        # Count frequency of each element
        frequency = Counter(nums)
        total_sum = 0

        # Sum elements whose frequency is divisible by k
        for num, freq in frequency.items():
            if freq % k == 0:
                total_sum += num * freq

        return total_sum