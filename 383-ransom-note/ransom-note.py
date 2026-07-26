class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) == 0:
            return True
        
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        r_dict = {}
        m_dict = {}

        for i in ransomNote:
            r_dict[i] = r_dict.get(i, 0) + 1
            
        for j in magazine:
            m_dict[j] = m_dict.get(j, 0) + 1
            
        for i in r_dict:
            if i not in m_dict or r_dict[i] > m_dict[i]:
                return False
        
        return True
            
#Optimal (HashMap)

#Count frequency of characters in ransomNote
#Count frequency of characters in magazine
#Every required character must exist in sufficient quantity
#Any shortage? → can't construct
#All counts satisfied → return True

#TC → O(n + m)
#SC → O(1)  (at most 26 lowercase letters)
        
        