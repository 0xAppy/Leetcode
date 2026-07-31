class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1

        haystack = list(haystack)

        h, n = 0, 0

        while h < len(haystack):

            if haystack[h] == needle[n]:
                if (''.join(haystack[h:h + len(needle)])) == needle:
                    return h
            
            h += 1
        
        return -1

#Brute

#Check every possible starting position
#First character matches? → compare full substring
#Full match? → return starting index
#No match? → try next position
#Never found? → return -1

#TC → O((n - m + 1) × m)
#SC → O(m)