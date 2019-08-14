class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profits = []
        #forward get the max
        p1 = 0
        current_min = prices[0]
        for price in prices:
            #update min
            current_min = min(current_min, price)
            p1 = max(p1, price - current_min)
            profits.append(p1)
        
        p2 = 0
        total = 0
        #traverse 
        current_max = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            current_max = max(current_max, prices[i])
            p2 = max(p2, current_max - prices[i])
            #update total sum 
            total = max(total, p2+profits[i])
        return total
        
        