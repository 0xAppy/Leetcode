class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        richie_rich = 0

        for i in accounts:
            richie_rich = max(richie_rich, sum(i))

        return richie_rich

        