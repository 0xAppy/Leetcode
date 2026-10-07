class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        return sum((i if i%m else -i for i in range(1,n+1)))




# BEFORE OPTIMIZE -->
# return sum((i for i in range(1,n+1) if i%m)) - sum((i for i in range(1,n+1) if i%m == 0))
# #00:04 & 00:08
        
        