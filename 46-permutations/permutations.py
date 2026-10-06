class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        def wrap(nums, current, result, used):
            # base case
            if len(current) == len(nums):
                result.append(current.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                current.append(nums[i])
                used[i] = True

                wrap(nums, current, result, used)

                current.pop()
                used[i] = False

        result = []
        used = [False] * len(nums)
        wrap(nums, [], result, used)

        return result

#Optimal (Backtracking)

#Build permutation one element at a time
#used[i] → prevents choosing the same index twice
#Choose number → add it to current permutation
#Recurse → continue building
#Complete permutation? → copy it into result
#Backtrack → remove last number and mark it unused

#TC → O(n × n!)
#SC → O(n)  (recursion + current + used, excluding output)