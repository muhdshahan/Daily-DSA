# 3668. Restore Finishing Order

## Problem Description

You are given an integer array order of length n and an integer array friends.

- order contains every integer from 1 to n exactly once, representing the IDs of the participants of a race in their finishing order.

- friends contains the IDs of your friends in strictly increasing order. Each ID in friends is guaranteed to appear in order.

Return an array containing your friends' IDs in their finishing order.

---

## Example

### Example 1

**Input:**  
`order = [3,1,2,5,4], friends = [1,3,4]`  
**Output:**  
`[3,1,4]`  

**Explanation:**  
- The finishing order is `[3, 1, 2, 5, 4]`. Therefore, the finishing order of your friends is `[3, 1, 4]`.

---

### Example 2

**Input:**  
`order = [1,4,5,3,2], friends = [2,5]`  
**Output:**  
`[5,2]`  

**Explanation:**  
- The finishing order is `[1, 4, 5, 3, 2]`. Therefore, the finishing order of your friends is `[5, 2]`.

---

## Constraints

- `1 <= n == order.length <= 100`
- order contains every integer from 1 to n exactly once
- `1 <= friends.length <= min(8, n)`
- `1 <= friends[i] <= n`
- friends is strictly increasing

---

## Approach

This problem can be solved using a simple filtering approach:
1. Since the list order already represents the participants’ finishing order, iterate through it directly.
2. For each participant id in order, check if it exists in friends.
3. Collect all such ids — this automatically preserves the original finishing order.

This approach has a time complexity of O(n × m),
where n is the length of order and m is the number of friends (≤ 8, so very small).

---

## Code Implementation (Python)

```python
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [ id for id in order if id in friends ]
```

----

## Acceptance

![Acceptance](https://github.com/muhdshahan/Daily-DSA/blob/main/3668-restore-finishing-order/acceptance.png)

