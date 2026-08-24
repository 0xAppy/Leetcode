class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        my_set = set(nums)
        longest_result = 0
        for num in my_set:
            if num-1 not in my_set:
                value = num
                count = 1
                while value+1 in my_set:
                    count += 1
                    value += 1
                longest_result = max(longest_result,count)
            else:
                count = 0
        return longest_result
        