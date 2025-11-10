class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        rslt = [sum(task) for task in tasks]
        return min(rslt)