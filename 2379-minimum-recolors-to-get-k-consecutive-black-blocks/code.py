class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Initial count of 'W's in the first window of size k
        count = blocks[:k].count("W")
        min_op = count
        
        # Slide the window through the string
        for i in range(k, len(blocks)):
            if blocks[i-k] == "W":
                count -= 1
            if blocks[i] == "W":
                count += 1
            min_op = min(min_op, count)
        
        return min_op
