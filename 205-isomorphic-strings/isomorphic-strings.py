from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_ST, map_TS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in map_ST and map_ST[c1] != c2) or (c2 in map_TS and map_TS[c2] != c1):
                return False

            map_ST[c1] = c2
            map_TS[c2] = c1
        
        return True

#Optimal (HashMap)

#Map s → t and t → s to keep a one-to-one mapping
#Existing mapping mismatch? → False
#Update both mappings for every character
#All characters match consistently → True

#TC → O(n)
#SC → O(n)