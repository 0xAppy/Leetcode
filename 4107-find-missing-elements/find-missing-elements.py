class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(min(nums), max(nums)):
            if i not in nums:
                result.append(i)

        return result

#Brute

#Check every number between minimum and maximum
#Missing in array? → add to answer
#Repeat until entire range is checked

#TC → O((max - min) × n)
#SC → O(1)  (excluding output list)    