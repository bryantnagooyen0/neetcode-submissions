class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Initialize DP array
        dp = [amount + 1] * (amount + 1)

        #Initialize DP base case
        dp[0] = 0

        #for loop through the amounts
        for a in range(1, amount + 1):
            #for loop through coins
            for c in coins:
            # if amount - c is not negative
                if a - c >= 0:
            #do recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a - c])

        #return dp[amount] if dp[amount] has changed
        return dp[amount] if dp[amount] != amount + 1 else -1