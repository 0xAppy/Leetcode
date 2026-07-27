class Solution(object):
    def isPalindrome(self, x):
        num = x
        num_reverse = 0

        while num > 0:
            last_digit = num % 10
            num_reverse = (num_reverse * 10) + last_digit
            num //= 10
        return True if x == num_reverse else False
