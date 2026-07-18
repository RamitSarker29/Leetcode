class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        Profit = 0
        max_Profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                Profit = i - min_price
            if Profit > max_Profit:
                max_Profit = Profit
        return max_Profit