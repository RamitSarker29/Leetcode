class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_price = prices[0]
        current_profit = float('-inf')
        best_profit = 0
        for i in range(len(prices)) :
            if prices[i] < current_price :
                current_price = prices[i]
            if current_price < prices[i] :
                current_profit = prices[i] - current_price
                best_profit = max(best_profit , current_profit)
        return best_profit 


        