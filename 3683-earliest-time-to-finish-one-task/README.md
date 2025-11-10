# 3683. Earliest Time to Finish One Task

## Problem Description

You are given a 2D integer array tasks where tasks[i] = [si, ti].

Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.

Return the earliest time at which at least one task is finished.

---

## Example

### Example 1

**Input:**  
tasks = [[1,6],[2,3]]
**Output:**  
5

**Explanation:**  
The first task starts at time t = 1 and finishes at time 1 + 6 = 7. The second task finishes at time 2 + 3 = 5. You can finish one task at time 5.

---

### Example 2

**Input:**  
tasks = [[100,100],[100,100],[100,100]]
**Output:**  
200 

**Explanation:**  
All three tasks finish at time 100 + 100 = 200.

---

## Constraints

- 1 <= tasks.length <= 100
- tasks[i] = [si, ti]
- 1 <= si, ti <= 100

---

## Approach

1. Iterate through each task in the tasks list — where each task is a list of numbers.
2. Compute the total time for each task by summing its elements using sum(task).
3. Store all these total times in a list called rslt.
4. Find the earliest possible completion time by returning the minimum value from rslt using min(rslt).
This approach ensures that the function determines the task which can be completed in the shortest total time by comparing the summed durations of all tasks.

---

## Code Implementation (Python)

```python
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        rslt = [sum(task) for task in tasks]
        return min(rslt)
```

----

## Acceptance

![Acceptance](https://github.com/muhdshahan/Daily-DSA/blob/main/3683-earliest-time-to-finish-one-task/acceptance.png)
