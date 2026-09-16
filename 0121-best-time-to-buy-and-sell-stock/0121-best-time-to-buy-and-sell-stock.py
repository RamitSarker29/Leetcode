class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        max_profit = 0
        for i in range(len(prices)) :
            if prices[i] < buy :
                buy = prices[i]
            else :
                profit = prices[i] - buy
                max_profit = max(max_profit , profit)
        return max_profit
        