class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        temp = []
        index = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break 

        print(index)

        if index == - 1:
            nums.reverse() #modify in place
            return 
            
        for j in range(n-1, index, -1):
            if nums[j] > nums[index]:
                nums[j], nums[index] = nums[index], nums[j]
                break

        print(nums)

        nums[index + 1:] = nums[index+1:][::-1]
        
        return # modify nums inpace and returned!!

#Optimal (Greedy + Two Pointers)

#Find first decreasing position from the right → nums[i] < nums[i+1]
#No such position? → array is descending, reverse it
#Find the rightmost number greater than nums[index]
#Swap them → makes the permutation slightly larger
#Reverse the suffix → make remaining part as small as possible
#Result = immediate next lexicographical permutation

#TC → O(n)
#SC → O(1)  (ignoring slice space)