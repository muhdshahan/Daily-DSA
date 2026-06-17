class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        min_value = 999
        min_index = 999
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                if min_value > capacity[i]:
                    min_value = capacity[i]
                    min_index = i
        return min_index if min_index != 999 else -1