class Solution:
    def maxDepth(self, s: str) -> int:
        
        count = 0
        result = 0

        for ch in s:
            if ch == "(":
                count += 1
                if count > result:
                    result = count
            elif ch == ")":
                count -= 1
        
        return result

#Optimal (Greedy / Counting)

#count = current parenthesis depth
#"(" → increase depth
#")" → decrease depth
#Track the maximum depth reached
#Maximum count = answer

#TC → O(n)
#SC → O(1)