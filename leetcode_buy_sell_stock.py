"""Since only need one transction, so we only need to find the min/max through a time sequence"""

#use DP to update the solution through iteration
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initial maximum profit to 0
        maximum_profit = 0
        #initial price to inifinite
        minimum_price = int(100000000000000)
        for i in prices:
            """two conditions, if this is the minimum, if the maximum, calculate the maximum profit so far"""
            if i < minimum_price:
                minimum_price = i
            else:
                maximum_profit = max(maximum_profit, i - minimum_price)
        return maximum_profit