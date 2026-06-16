class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        freq_pairs = Counter(n)
        n = set(n)
        rslt = 0
        for i in n:
            rslt += int(i) * freq_pairs[i]
        return rslt