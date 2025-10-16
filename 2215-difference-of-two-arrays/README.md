# 2215. Find the Difference of Two Arrays

## Problem Description

Given two **0-indexed** integer arrays `nums1` and `nums2`, return a list `answer` of size 2 where:

- `answer[0]` is a list of all **distinct integers** in `nums1` which are **not present** in `nums2`.
- `answer[1]` is a list of all **distinct integers** in `nums2` which are **not present** in `nums1`.

> Note: The integers in the lists may be returned in **any order**.

---

## Example

### Example 1

**Input:**  
`nums1 = [1,2,3], nums2 = [2,4,6]`  
**Output:**  
`[[1,3],[4,6]]`  

**Explanation:**  
- In `nums1`, elements `1` and `3` are not present in `nums2`.  
- In `nums2`, elements `4` and `6` are not present in `nums1`.

---

### Example 2

**Input:**  
`nums1 = [1,2,3,3], nums2 = [1,1,2,2]`  
**Output:**  
`[[3],[]]`  

**Explanation:**  
- In `nums1`, the value `3` does not appear in `nums2`.  
- All integers in `nums2` are present in `nums1`, so the second list is empty.

---

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`  
- `-1000 <= nums1[i], nums2[i] <= 1000`

---

## Approach

This solution uses a **simple iteration** approach with final **set conversion** to remove duplicates.

1. Iterate through `nums1`, and add elements **not in** `nums2` to a list.
2. Do the same for `nums2` by checking if elements **not in** `nums1`.
3. Convert both resulting lists to sets (to remove duplicates), then back to lists for the final result.

---

## Code Implementation (Python)

```python
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        rslt = []
        for i in nums1:
            if i not in nums2:
                rslt.append(i)

        r = []
        for i in nums2:
            if i not in nums1:
                r.append(i)

        return [list(set(rslt)), list(set(r))]

