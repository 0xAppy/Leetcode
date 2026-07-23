class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        maxi = 0
        left, right = 0, 0
        my_dict = {}

        while right < n:
            
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)

            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1

            

        return maxi

#Sliding window → maintain unique substring
#right expands window, left shrinks on duplicate
#Duplicate found → jump left after previous occurrence
#max(left, ...) prevents moving left backward
#Window size = right - left + 1
#Store latest index of every character
#Keep updating maximum window length