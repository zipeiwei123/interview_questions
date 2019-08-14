#if next > previous, add the gain, greedy alike?

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #special case
        if not prices:
            return 0
        max_profits = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profits += prices[i] - prices[i-1]
        return max_profits
        