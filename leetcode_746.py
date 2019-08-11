"""DP, use an array to keep track current value
    Return Minimum of the last and second-last stair's cost"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #special condtion 
        if len(cost) <= 1 or len(cost) > 1000:
            return -1
        dp = [-1]*len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        return min(dp[-1], dp[-2])
        