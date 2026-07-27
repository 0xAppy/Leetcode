class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 3:
            return [0, 1, 1][x]

        ans = 0 
        
        l, r = 0, x//2

        while l <= r:
            
            m = (l + r) // 2

            if m * m <= x:
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans

#Answer lies between 0 and x/2
#Binary search on possible square root
#Square fits? → save answer and try bigger number
#Square too large? → search smaller numbers
#Last valid number = floor of √x

#TC → O(log x)
#SC → O(1)