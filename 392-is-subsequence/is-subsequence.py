class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        result = False
        
        t_char = list(t)
        s_char = list(s)

        i, j = 0, 0
        
        while i < len(s_char) and j < len(t_char):

            if s_char[i] == t_char[j]:
                j += 1
                i += 1
            else:
                j += 1


        return i == len(s_char)

#Optimal (Two Pointers)

#One pointer for s, one for t
#Match found? → move both pointers
#No match? → move only t pointer
#If all characters of s are matched → valid subsequence

#TC → O(|t|)
#SC → O(1)