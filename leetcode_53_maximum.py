"""Use divide and conquer"""
"""Having an array that stores local solution, and the maximum profit stores maximum profit
   Iterate through the nums, update local and maximum number"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #first check special case
        if not nums:
            return 0
#         #set up maximum profit to infinite
#         maximum_profit = float("-inf")
#         #create a dp array to store the previous solution
#         dp = [0 for number in nums]
#         #iterat through nums
#         for index in range(len(nums)):
#             #DP CONDITIOMS, Most important, local maximum
#             dp[index] = max(dp[index-1] + nums[index], nums[index])
#             #update global max
#             maximum_profit = max(dp[index], maximum_profit)
#         return maximum_profit
        """Two ways, use an variable instead of array"""
        #set up maximum profit to infinite
        maximum_profit = float("-inf")
        #use a single varible to update current sum
        current_sum = float("-inf")
        for index in range(len(nums)):
            if current_sum + nums[index] < nums[index]:
                current_sum = nums[index]
            else:
                current_sum += nums[index]
            maximum_profit = max(maximum_profit, current_sum)
        return maximum_profit