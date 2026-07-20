class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ''.join(c.lower() for c in s if c.isalnum())

        return result == result[::-1]

#Optimal

#Keep only letters and digits
#Convert everything to lowercase
#Compare string with its reverse
#Same? → palindrome, else not

#TC → O(n)
#SC → O(n)