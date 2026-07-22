class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k

#Optimal (Two Pointers)

#k tracks the next valid position
#Skip elements equal to val
#Keep valid elements at the front
#Return count of valid elements

#TC → O(n)
#SC → O(1)