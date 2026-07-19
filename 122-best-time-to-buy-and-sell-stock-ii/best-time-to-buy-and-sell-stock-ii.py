class Solution:
    def maxProfit(self, prices: List[int]):

        profit = 0

        buy = 0
        sell = 1

        while buy < len(prices) and sell < len(prices):

            if prices[buy] < prices[sell]:
                profit += prices[sell] - prices[buy]
                buy = sell
                sell += 1
            elif prices[buy] > prices[sell]:
                buy = sell
            else:
                sell += 1

        return profit

#Optimal (Two Pointers)

#One pointer for s, one for t
#Match found? → move both pointers
#No match? → move only t pointer
#If all characters of s are matched → valid subsequence

#TC → O(|t|)
#SC → O(1)