class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        nums.sort()

        for l in range(0, len(nums), 2):
            r = l + 1
            nums[l], nums[r] = nums[r], nums[l]
                    
        return nums

#Optimal (Greedy + Sorting)

#Sort numbers → smallest pairs come together
#Take 2 numbers at a time
#Swap them → smaller goes after larger
#Repeat for every pair
#Return the modified array

#TC → O(n log n)
#SC → O(1)  (ignoring sorting space)