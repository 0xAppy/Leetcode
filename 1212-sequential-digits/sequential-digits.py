class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(nums)
        i, j = 0, 0
        all_nums = []
        result = []

        for i in range(n):
            for j in range(i, n): 
                lst = nums[i:j+1]
                
                num = int(''.join(map(str, lst)))
                all_nums.append(num)
        
        for i in all_nums:
            if low <= i and i <= high:
                result.append(i)

        return sorted(result)
        
#Brute

#Generate every possible sequential number
#Join consecutive digits to form a number
#Keep only numbers within the given range
#Sort valid numbers before returning

#TC → O(1)  (Only 45 numbers are generated)
#SC → O(1)
        