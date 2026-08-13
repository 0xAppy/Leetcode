class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


#Better

#split() → removes extra spaces + gives words
#Reverse the word list
#join() → puts words back with single spaces
#Done → words reversed, spaces cleaned

#TC → O(n)
#SC → O(n) --> O(1) in Optimal