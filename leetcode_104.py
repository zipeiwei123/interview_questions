"""Use two ways, recursive, DFS with stack"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # else:
        #     l_depth = self.maxDepth(root.left)
        #     r_depth = self.maxDepth(root.right)
        #     return max(l_depth,r_depth)+1
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        maximum_depth = 0
        while stack:
            current_node, current_depth = stack.pop()
            if current_depth > maximum_depth:
                maximum_depth = current_depth
            if current_node.left:
                stack.append((current_node.left, current_depth + 1))
                
            if current_node.right:
                stack.append((current_node.right, current_depth + 1))
        return maximum_depth
                