class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split()):
            return False

        if len(set(list(pattern))) != len(set(s.split())):
            return False

        split_s = s.split()

        my_dict = {}

        i=0

        while i < len(pattern):

            my_dict[i] = pattern[i], split_s[i]

            i += 1

        unique_values = set(my_dict.values())
        
        return len(unique_values) == len(set(list(pattern)))

