class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        c, v = 0, 0
        for i in s:
            if i in vowels:
                v+=1
            elif i.isalpha():
                c+=1
        if c==0:
            return 0
        return floor(v/c)