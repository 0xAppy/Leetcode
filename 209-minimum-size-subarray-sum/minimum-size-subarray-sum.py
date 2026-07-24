class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, total = 0, 0
        diff = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                diff = min(diff, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if diff == float('inf') else diff
    

#Optimal (Sliding Window)

#Expand window until sum reaches target
#Target reached? → shrink from left
#Keep shrinking to find the smallest valid window
#Update minimum length whenever window is valid
#Return 0 if no valid subarray exists

#TC → O(n)
#SC → O(1)

        