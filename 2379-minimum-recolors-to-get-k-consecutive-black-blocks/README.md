# 2379. Minimum Recolors to Get K Consecutive Black Blocks

## Problem Description

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the i-th block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block ('W') such that it becomes a black block ('B').

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

---

## Example

### Example 1

**Input:**  
blocks = "WBBWWBBWBW", k = 7
**Output:**  
3

**Explanation:**  
- One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks so that blocks = "BBBBBBBWBW".
- It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.

---

### Example 2

**Input:**  
`blocks = "WBWBBBW", k = 2`  
**Output:**  
`0`  


---

## Constraints

- n == blocks.length
- 1 <= n <= 100
- blocks[i] is either 'W' or 'B'
- 1 <= k <= n

---

## Approach

This solution uses a sliding window approach:

1. Count the number of 'W' characters in the first k characters of blocks. This is the number of recolors needed for the first window.
2. Slide the window one block at a time from left to right:
    - If the character leaving the window is 'W', decrement the count.
    - If the new character entering the window is 'W', increment the count.
3. Keep track of the minimum count seen during the sliding process.
4. Return this minimum as it represents the minimum number of recolors needed to get k consecutive black blocks.

---

## Code Implementation (Python)

```python
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


