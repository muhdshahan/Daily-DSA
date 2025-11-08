# 2032. Two Out of Three

## Problem Description

Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

---

## Examples

### Example 1

**Input:**  
nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
**Output:**  
[3,2]

**Explanation:**  
The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

---

### Example 2

**Input:**  
nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
**Output:**  
[2,3,1]

**Explanation:**  
The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

---

### Example 3

**Input:**  
nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
**Output:**  
[]

**Explanation:**  
No value is present in at least two arrays.

---

## Constraints

- 1 <= nums.length <= 100
- 1 <= nums1.length, nums2.length, nums3.length <= 100

---

## Approach

1. Remove Duplicates:
    - Convert each of the three lists (nums1, nums2, and nums3) into sets to ensure that each element is counted only once per list.
2. Combine and Count:
    - Merge all three sets into a single list and use a frequency counter (Counter) to count how many different lists each number appears in.
3. Filter Elements Appearing in At Least Two Lists:
    - Iterate through the counter and select elements whose frequency is greater than 1, meaning they appear in at least two out of the three lists.
4. Return the Result:
    - Collect these qualifying elements in a result list and return it as the final output.

---

## Code Implementation (Python)

```python
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        num = Counter(num)
        reslt = []
        for key in num:
            if num[key]>1:
                reslt.append(key)
        return reslt
```

----

## Acceptance

![Acceptance](https://github.com/muhdshahan/Daily-DSA/blob/main/2032-two-out-three/acceptance.png)
