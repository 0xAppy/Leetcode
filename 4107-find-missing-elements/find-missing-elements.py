class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low, high = min(nums), max(nums)
        set_nums = set(nums)
        return [x for x in range(low, high) if x not in set_nums]

#Optimal (HashSet)

#Store min and max once
#Convert array into a set for O(1) lookup
#Check every number between low and high
#Missing in set? → add to answer

#TC → O(n + (high - low))
#SC → O(n)
