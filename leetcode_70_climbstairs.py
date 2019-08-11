"""Two ways recursicve call with memorization"""

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         #use an array to store each combination until n
#         memo = [0]*(n+1)
#         return self.climb_stairs(0, n, memo)
    
#     def climb_stairs(self, current_step, n, memo):
#         if (current_step > n):
#             return 0
#         elif (current_step == n):
#             #get a solution
#             return 1
        
#         #This is where the recursive come in, and find the memorization step
#         elif (memo[current_step] > 0):
#             return memo[current_step]
        
#         memo[current_step] = self.climb_stairs(current_step + 1, n, memo) + self.climb_stairs(current_step + 2, n, memo)
#         return memo[current_step]
class Solution:
    def climbStairs(self, n: int) -> int:
        """Broke the whole problem into smaller problem"""
        if(n == 1):
            return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

