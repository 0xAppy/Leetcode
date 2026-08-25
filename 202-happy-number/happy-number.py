import math
class Solution:
    def isHappy(self, n: int) -> bool:

        if n <= 0:
            return False
        
        my_set = set()

        while n != 1:
            Sum = 0
            if n in my_set:
                return False
            my_set.add(n)
            
            for num in str(n):
                Sum += int(num) ** 2
                
            n = Sum
        
        return True

        

        

        