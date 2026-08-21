from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        sort_s = []

        for s in strs:
            sort_s.append(sorted(s))

        print(sort_s)

        groups = {}

        for i, item in enumerate(sort_s):
            key = tuple(item)
            groups.setdefault(key, []).append(i)

        result = [
                [strs[i] for i in indexes]
                for indexes in groups.values()
            ]
        
        return result

#Better (Hashing + Sorting)

#Sort each word → anagram words get the same key
#Use sorted characters as the hashmap key
#Same key? → put words into the same group
#Store indexes → use them to rebuild original words
#Return all anagram groups

#TC → O(n × m log m)  (m = average word length)
#SC → O(n × m)