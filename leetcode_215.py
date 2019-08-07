class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums:
            #first sort the array
            nums.sort()
            #second return the kth largest element
            return nums[len(nums) - k]
           
        else:
            return 0