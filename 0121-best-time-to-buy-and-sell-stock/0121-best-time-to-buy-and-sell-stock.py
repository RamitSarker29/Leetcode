class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = prices[0]

        for current_price in prices:
            lowest_buy = min(lowest_buy, current_price)
            profit = current_price - lowest_buy
            max_profit = max(max_profit, profit)

        return max_profit