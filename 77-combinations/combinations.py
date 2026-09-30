class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        result = []

        def backtrack(start, combo):

            if len(combo) == k:
                result.append(combo.copy())
                return

            for i in range(start, n+1):
                combo.append(i)
                backtrack(i+1, combo)
                combo.pop()
            
        backtrack(1, [])
        return result
        
# 00:22
#Optimal (Backtracking)

#Start from 1 → choose numbers one by one
#backtrack(i + 1) → ensures numbers are not reused
#When combo reaches size k → store a copy
#pop() → undo the choice and try the next number

#TC → O(C(n, k) × k)
#SC → O(k)  (recursion + current combination, excluding output)