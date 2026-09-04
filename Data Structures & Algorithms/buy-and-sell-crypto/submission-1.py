class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float("inf")

        for day_price in prices:
            min_buy=min(min_buy, day_price)
            max_profit = max(max_profit, day_price-min_buy)
        return max_profit
            