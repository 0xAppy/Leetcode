class Solution:
    def largestOddNumber(self, num: str) -> str:

        n = len(num)

        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[0:i+1]
        
        return ""

#Optimal (Greedy)

#Scan from the end → last digit decides if number is odd
#Odd digit found? → everything before it forms the largest odd number
#No odd digit? → return empty string

#TC → O(n)
#SC → O(1)
        