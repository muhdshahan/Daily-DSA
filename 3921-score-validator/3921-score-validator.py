class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for element in events:
            if element == "W":
                counter+=1
            elif element == "WD":
                score+=1
            elif element == "NB":
                score +=1
            else:
                score += int(element)
            if counter==10:
                return [score, counter]
        return [score, counter]