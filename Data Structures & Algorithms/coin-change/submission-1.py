class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [0] + [float('inf')] * amount

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    amounts[i] = min(amounts[i], amounts[i - c] + 1)

        return -1 if amounts[amount] == float('inf') else amounts[amount]