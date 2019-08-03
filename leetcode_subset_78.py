""" Apply back tracking  on visiited index ??? """
""" if the question is asking for returning all the subset, it most likely is a dfs"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == None:
            return []
        else:
            duplicate_subsets = []
            subset = []
            index = 0
            self.dfs_backtracking(nums, subset, duplicate_subsets,  index)
            return duplicate_subsets
    
    """A recusive called function"""
    def dfs_backtracking(self, nums, subset, duplicate_subsets,  index):
        #stop condition
        if index == len(nums):
            print("the current subset is", subset)
            duplicate_subsets.append(subset[:])
            return
        
        self.dfs_backtracking(nums, subset, duplicate_subsets, index+1)
        #if we visit this index
        print("index is ", nums[index])
        subset.append(nums[index])
        self.dfs_backtracking(nums, subset, duplicate_subsets, index+1)
        #back tracking
        subset.remove(nums[index])
        # for i in range(index, len(nums)):
        #     #add all the leaf nodes
        #     subset.append(nums[index])
        #     self.dfs_backtracking(nums, subset, duplicate_subsets, index+1)
        #     #back tracking
        #     subset.remove(nums[index])