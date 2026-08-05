class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first = strs[0]

        result = []

        for i in range(len(first)):
            for word in strs:
                if i >= len(word) or first[i] != word[i]:
                    return first[:i]
        return first

#Optimal

#Take first string as reference
#Compare each character with every other string
#Mismatch or shorter word? → prefix ends here
#No mismatch? → entire first string is the common prefix

#TC → O(n × m)  (n = number of strings, m = length of prefix/first string)
#SC → O(1)