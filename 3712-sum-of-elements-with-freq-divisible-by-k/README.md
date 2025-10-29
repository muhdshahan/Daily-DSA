# 3712. Sum of Elements With Frequency Divisible by K

## Problem Description

You are given an integer array nums and an integer k.

Return an integer denoting the sum of all elements in nums whose frequency is divisible by k, or 0 if there are no such elements.

Note: An element is included in the sum as many times as it appears in the array if its total frequency is divisible by k.

---

## Example

### Example 1

**Input:**  
nums = [1,2,2,3,3,3,3,4], k = 2
**Output:**  
16

**Explanation:**  
- The number 1 appears once → frequency 1 (not divisible by 2).
- The number 2 appears twice → frequency 2 (divisible by 2).
- The number 3 appears four times → frequency 4 (divisible by 2).
- The number 4 appears once → frequency 1 (not divisible by 2).
Total sum = 2 + 2 + 3 + 3 + 3 + 3 = 16.

---

### Example 2

**Input:**  
nums = [1,2,3,4,5], k = 2
**Output:**  
0 

**Explanation:**  
All elements appear once (frequency = 1).
Since no frequency is divisible by 2, the result is 0.

---

## Constraints

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100

---

## Approach

1. Count the frequency of each element in nums using a frequency map (Counter).
2. Iterate through each unique element and its frequency:
    - If the frequency is divisible by k, include that element’s total contribution in the sum (element * frequency).
3. Return the total sum after checking all elements.
This approach ensures all valid elements are added as many times as they appear, maintaining the frequency logic.

---

## Code Implementation (Python)

```python
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
```

----

## Acceptance

![Acceptance](https://github.com/muhdshahan/Daily-DSA/blob/main/3712-sum-of-elements-with-freq-divisible-by-k/Acceptance.png)