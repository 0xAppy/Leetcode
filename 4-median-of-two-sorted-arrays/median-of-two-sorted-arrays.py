class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)

        if n % 2 == 1:
            return nums[n // 2]
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2

# 00:14
#Brute

#Combine both sorted arrays
#Sort the entire combined array
#Find the middle element(s)
#Odd length → one middle element
#Even length → average of two middle elements

#TC → O((m + n) log(m + n))
#SC → O(m + n)