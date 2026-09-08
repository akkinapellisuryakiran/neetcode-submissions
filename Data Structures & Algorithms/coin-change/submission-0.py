class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for current in range(1, amount+1):
            for coin in coins:
                if coin <= current:
                    dp[current] = min(
                        dp[current],
                        1 + dp[current-coin]
                    )
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]