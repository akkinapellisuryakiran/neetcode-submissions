class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_buy = prices[0]

        for day_price in prices[1:]:
            if min_buy < day_price:
                max_profit = max(max_profit, day_price-min_buy)
                continue
            min_buy=day_price
        return max_profit
            