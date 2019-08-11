"""Two ways, brute force and DP
    if is true if index i in s in wordDict, and s[i:j] is a word in word Dict"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #create a dp array for true and false
        dp = [False]*(len(s) + 1)
        #set DP index true
        dp[0] = True
        for i in range(1, len(s) + 1):
            #define the j from i to 0
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
             
        return dp[len(s)]
     
    