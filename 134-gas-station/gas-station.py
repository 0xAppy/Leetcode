class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        ## Not Enough Fuel
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)

        total = 0
        start = 0

        for i in range(n):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1
        
        return start

#Optimal (Greedy)

#Total gas < total cost? → impossible
#total tracks fuel left from current start
#Fuel goes negative? → current start can't work
#Reset fuel and try next station as start
#If total fuel is enough, the remaining start is valid

#TC → O(n)
#SC → O(1)