"""Define the longest substring
   a condition to check if substring is a panlindrone
   Use a N by N matrix to check if the index is palindrome"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #special case
        if not s:
            return ""
        iAns, jAns = 0, 0
        #create a matrix for keep tracking
        matrix = [[False]*len(s) for i in range(len(s))]
        #first set all the diagonal to True a==a
        for i in range(len(s)):
            matrix[i][i] = True
        #first check for case 2, if "ab", "aa"
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        #case 3, only needs to check start and end
        for start in range(3, len(s)+1):
            for end in range(0, len(s) - start + 1):
                if s[end] = s[end + start -1] and matrix[end + 1][end + (start - 2)]:
                    matrix[end][end + (start - 1)] = True
                    iAns = end
                    jAns = end + (start - 1)
        return s[iAns:jAns+1]
     
   
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         iAns = 0
#         jAns = 0
#         for i in range(n):
#             dp[i][i] = True
#             iAns = i
#             jAns = i
#         for i in range(n - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 iAns = i
#                 jAns = i + 1
#         for ln in range(3, n + 1):
#             for i in range(0, n - (ln - 1)):
#                 if s[i] == s[i + (ln - 1)] and dp[i + 1][i + (ln - 2)]:
#                     dp[i][i + (ln - 1)] = True
#                     iAns = i
#                     jAns = i + (ln - 1)
#         return s[iAns:jAns + 1]