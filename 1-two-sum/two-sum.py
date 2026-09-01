class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        freq = {}
        for i in range(0,n):
            left = target - nums[i]
            if left in freq:
                return (freq[left],i)
            freq[nums[i]] = i