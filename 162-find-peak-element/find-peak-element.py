class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        n = len(nums)
        left, right = 0, n-1
        target = 0

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid

        return left

# 00:08
#Optimal (Binary Search)

#Compare nums[mid] with nums[mid + 1]
#Increasing slope → peak is on the right
#Decreasing slope → peak is at mid or on the left
#Keep shrinking the search space
#When left == right → peak index found

#TC → O(log n)
#SC → O(1)
        