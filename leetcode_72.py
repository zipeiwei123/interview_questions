"""Use Matrix n*p to stores the words"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #special case if one of the word is empty
        if len(word1)*len(word2) == 0:
            return len(word1)+len(word2)
        #create DP matrix
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        #initiate boundaries
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        
        #DP solution
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                #cost to move left, right, top, down
                left = dp[i-1][j] + 1
                down = dp[i][j-1] + 1
                left_down = dp[i-1][j-1] 
                #if the two words are equal, then no cost for left_down
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)
        
        return dp[len(word1)][len(word2)]
#         n = len(word1)
#         m = len(word2)
        
#         # if one of the strings is empty
#         if n * m == 0:
#             return n + m
        
#         # array to store the convertion history
#         d = [ [0] * (m + 1) for _ in range(n + 1)]
        
#         # init boundaries
#         for i in range(n + 1):
#             d[i][0] = i
#         for j in range(m + 1):
#             d[0][j] = j
        
#         # DP compute 
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 left = d[i - 1][j] + 1
#                 down = d[i][j - 1] + 1
#                 left_down = d[i - 1][j - 1] 
#                 if word1[i - 1] != word2[j - 1]:
#                     left_down += 1
#                 d[i][j] = min(left, down, left_down)
        
#         return d[n][m]