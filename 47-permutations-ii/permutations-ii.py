class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
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

        print(result)
        #REMOVE DUPS
        result = list(set(map(tuple, result)))
        result = [list(x) for x in result]
        print(result)
        return result

#Better (Backtracking + Set)

# Just Permutation + remove dups

#TC → O(n × n!)  (can be worse with duplicates due to extra generated permutations)
#SC → O(n × n!)  (stored permutations + set, excluding recursion)