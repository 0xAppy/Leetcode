class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = {}

        for i in range(n):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
            
        max_key = max(my_dict, key=my_dict.get)
        return max_key

        