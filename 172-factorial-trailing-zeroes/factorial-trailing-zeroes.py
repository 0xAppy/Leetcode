class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0

        while n > 0:
            n //= 5
            count += n
        
        return count

# 00:12
#Optimal (Math)

#Trailing zeros come from factors of 10 = 2 × 5
#There are always more 2s than 5s in n!
#So count how many factors of 5 exist
#n // 5 → count multiples of 5
#n // 25 → count extra 5 from multiples of 25
#Keep dividing by 5 until n becomes 0

#TC → O(log₅ n)
#SC → O(1)

        