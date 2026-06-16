class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        freq_pairs = Counter(n)
        rslt = 0
        for i in freq_pairs:
            rslt += int(i) * freq_pairs[i]
        return rslt