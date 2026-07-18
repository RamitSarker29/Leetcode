class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest_buy=prices[0]
        for i in prices:
            current_price=i
            lowest_buy=min(lowest_buy,current_price)
            profit=current_price-lowest_buy
            max_profit=max(max_profit,profit)
        return max_profit