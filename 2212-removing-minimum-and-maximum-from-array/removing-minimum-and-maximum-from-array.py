class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        min_pos = nums.index(min(nums)) 
        max_pos = nums.index(max(nums))

        n = len(nums)

        # Scenario:1 - Both removed from left 
        case_1 = max(min_pos, max_pos) + 1
        
        # Scenario:2 - Both removed from right
        case_2 = n - min(min_pos, max_pos)

        # Scenario:3 - One from left and one from right
        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)
        case_3 = (left + 1) + (n - right)

        return min(case_1, case_2, case_3)


#Optimal (Greedy)

#Find positions of min and max
#3 choices: remove both from left, both from right, or one from each side
#Calculate deletions for all 3 cases
#Take the minimum

#TC → O(n)
#SC → O(1)