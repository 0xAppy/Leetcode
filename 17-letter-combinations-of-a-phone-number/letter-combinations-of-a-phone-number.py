class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        char_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def dfs(i, subset):
            if i == len(digits):
                res.append("".join(subset.copy()))
                return
            
            for ch in char_map[digits[i]]:
                subset.append(ch)

                # include
                dfs(i+1, subset)
                subset.pop()      

        dfs(0, [])
        return res