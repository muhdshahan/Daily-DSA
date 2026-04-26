class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        bulb_list = Counter(bulbs)
        on_bulbs = [ x for x in bulb_list if bulb_list[x]%2==1 ]
        return sorted(on_bulbs)