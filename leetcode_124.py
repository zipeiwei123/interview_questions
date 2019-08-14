"""????"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #initial the max gain variable
        max_gain = float("-inf")
        #call get max gain start from root
        max_gain = self.get_max_gain(root, max_gain)
        return max_gain
    
    def get_max_gain(self, node, max_gain):
        #if node is none
        if not node:
            return 0
        #get max from left and right branch
        left_gain = max(self.get_max_gain(node.left, max_gain), 0)
        right_gain = max(self.get_max_gain(node.right, max_gain), 0)
            
        #get current gain starts from current ndoe
        current_gain = node.val + left_gain + right_gain
        #update max_gain
        max_gain = max(current_gain, max_gain)
        #For recusion?
        return node.val + max(left_gain, right_gain)
            
        
    