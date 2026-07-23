class Solution(object):
    def twoSum(self, numbers, target):
        nums = numbers
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining]+1, i+1]
            hash_map[nums[i]] = i