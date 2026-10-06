class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def wrapper(x, n):
            if n == 0: return 1
            if x == 0: return 0

            result = wrapper(x * x, n // 2)

            return x * result if n % 2 else result

        result = wrapper(x, abs(n))
        return result if n >= 0 else 1/result

# 00:44
#Optimal (Binary Exponentiation)

#Square x → doubles the power each step
#n // 2 → cuts the remaining power in half
#Odd n? → multiply one extra x
#Repeat until n becomes 0
#Negative n? → take reciprocal at the end
#Power is reduced by half each recursive call

#TC → O(log n)
#SC → O(log n)  (recursion stack)