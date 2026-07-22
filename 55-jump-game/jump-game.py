class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        max_index = 0

        for i in range(n):
            
            if max_index < i:
                return False
                
            max_index = max(max_index, i + nums[i])
        
        return True

#max_index = farthest position reachable so far
#If current index is unreachable → game over
#At every step, try extending reachable range
#Keep updating farthest jump possible
#Reach every index? → last index is guaranteed reachable
#No need to actually perform jumps

#TC → O(n)
#SC → O(1)