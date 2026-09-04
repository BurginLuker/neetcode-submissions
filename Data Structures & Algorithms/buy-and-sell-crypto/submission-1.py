class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = prices[0]
        
        profit = 0
        for i in prices:
            small = min(i, small)
            profit = max(profit, i - small)

        return profit