class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        count = 0 
        result = ""

        for i in s:
            if i == "(":
                count += 1
                if count > 1:
                    result += i
            elif i == ")":
                count -= 1
                if count > 0:
                    result += i

        return result

#Optimal (Greedy)

#Track nesting depth with count
#Outer "(" → skip
#Inner "(" → keep
#Inner ")" → keep
#Outer ")" → skip

#TC → O(n)
#SC → O(n)  (output string)