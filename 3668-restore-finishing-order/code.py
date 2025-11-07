class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [ id for id in order if id in friends ]