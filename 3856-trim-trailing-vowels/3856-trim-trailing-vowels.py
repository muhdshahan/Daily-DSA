class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = 'aeiou'
        tr_len = 0
        for letter in s[::-1]:
            if letter in vowels:
                tr_len+=1
            else:
                return s[:len(s)-tr_len]
        return s[:len(s)-tr_len]