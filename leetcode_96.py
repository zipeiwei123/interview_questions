"""Break TSB into subproblem, select the unique root, then solve the unqiue root's subproblem"""

class Solution:
    def numTrees(self, n: int) -> int:
        #dp is number of solution
        dp = [0]*(n+1)
        dp[0] , dp[1] = 1, 1
        
        #select i as the unique root
        for i in range(2, n+1):
            #for each root, generate unique solution from root
            for j in range(1, i+1):
                #??why i-j
                dp[i] += dp[j-1] * dp[i-j]
            
        
        
        return dp[n]
        