class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = (s.split()[-1])
        n = len(last_word)
        return n