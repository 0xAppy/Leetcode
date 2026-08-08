class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}

        for i in s:
            my_dict[i] = my_dict.get(i, 0) + 1

        for i in range(len(s)):
            if my_dict[s[i]] == 1:
                return i

        return -1