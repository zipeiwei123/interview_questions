"""Union find is most likely to detect cycles, looks similar to dfs with backtracking"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set nums to set
        nums = set(nums)
        #use a dictionary to track each correspondence continous sequence
        tracking = {}
        #create longest continous numbers
        longest_numbers = 0
        for number in nums:
            #return longest numbers by iterate through number
            longest_numbers = max(longest_numbers, number - self.find(number, nums, tracking))
        return longest_numbers
    
    #A so called union find function, a recursive function for finding the longest numbers 
    def find(self, number, nums, tracking):
        #check if this is the end sequence from numbers
        if number in tracking and tracking[number] != number - 1:
            return tracking[number]
        #check if there is subsequence in numbers
        if number - 1 in nums:
            #set tracking
            tracking[number] = self.find(number - 1, nums, tracking)
            return tracking[number]
        else:
            return number - 1