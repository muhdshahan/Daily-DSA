class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        alice_limit = len(candyType)//2
        unique_types = len(set(candyType))
        return alice_limit if alice_limit < unique_types else unique_types