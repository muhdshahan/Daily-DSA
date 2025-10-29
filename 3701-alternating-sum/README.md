# 3701. Compute Alternating Sum

## Problem Description

You are given an integer array nums.

The alternating sum of nums is the value obtained by adding elements at even indices and subtracting elements at odd indices.
That is:
nums[0] - nums[1] + nums[2] - nums[3] + ...

Return an integer denoting the alternating sum of nums.

---

## Example

### Example 1

**Input:**  
nums = [1, 3, 5, 7]
**Output:**  
-4

**Explanation:**  
- Even indices → nums[0] = 1, nums[2] = 5
- Odd indices → nums[1] = 3, nums[3] = 7
The alternating sum is:
1 - 3 + 5 - 7 = -4

---

### Example 2

**Input:**  
nums = [100]
**Output:**  
100

**Explanation:**  
There is only one element (index 0, even), so the alternating sum is 100.

---

## Constraints

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

---

## Approach

1. Initialize a variable total to 0.
2. Traverse the array using indices.
3. If the index is even, add the element to total;
if odd, subtract it.
4. Return the resulting total.

This ensures alternate addition and subtraction according to the index positions.

---

## Code Implementation (Python)

```python
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_sum = sum([ nums[ind] for ind in range(len(nums)) if ind%2==0 ])
        odd_sum = sum([ nums[ind] for ind in range(len(nums)) if ind%2!=0 ])
        return even_sum - odd_sum
```

----

## Acceptance

![Acceptance](https://github.com/muhdshahan/Daily-DSA/blob/main/3701-alternating-sum/acceptance.png)