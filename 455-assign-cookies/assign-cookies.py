class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        result = 0 
        i, j = 0, 0
        curr_j = j

        s = sorted(s)
        g = sorted(g)

        while i < len(g) and j < len(s):
            
            if s[j] >= g[i]:
                i += 1
                result += 1

            j += 1

        return result

#optimal
#Sort both arrays → match smallest cookie with smallest greed
#Cookie big enough? → child is satisfied
#Satisfied child → move to next child
#Always move cookie pointer because cookie gets used
#Greedy match avoids wasting large cookies on small greed

#TC → O(n log n + m log m)
#SC → O(1)  (ignoring sorting space)