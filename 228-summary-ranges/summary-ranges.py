class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []
        l, r = 0, 0
        while l<len(nums) and r<len(nums):

            if r + 1 < len(nums) and nums[r] + 1 == nums[r+1]:
                r += 1
            else:
                if l == r:
                    result.append(str(nums[l]))
                    r += 1
                    l = r
                else:
                    result.append(str(nums[l]) + "->" + str(nums[r]))
                    r += 1
                    l = r

        return result 

#Optimal (Two Pointers)

#l marks the start of current range
#r keeps extending while numbers are consecutive
#Range breaks? → save single number or full range
#Move both pointers to start a new range
#Repeat until all numbers are covered

#TC → O(n)
#SC → O(1)  (excluding output list)