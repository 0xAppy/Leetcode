import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        zero_count = nums.count(0)
        total_product = 1 
        for num in nums:
            if num != 0:
                total_product *= num

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            for num in nums:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(total_product//num)

        return result

#Better

#Count zeros and multiply all non-zero numbers
#2+ zeros? → every result is 0
#1 zero? → only zero's position gets total product
#No zeros? → total product ÷ current number
#Handle zero cases separately to avoid division by zero

#TC → O(n)
#SC → O(n)  (output array)