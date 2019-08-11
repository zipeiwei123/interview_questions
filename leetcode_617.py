# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""Setup one tree as base tree, merge t2 into t1
   Two ways, recusive, iterative with DFS"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #special case
        if not t1:
            return t2
        stack = []
        stack.append((t1, t2))
        while stack:
            node1, node2 = stack.pop()
            #if t2 has value
            if node2:
                node1.val += node2.val
            if node1.left:
                stack.append((node1.left, node2.left))
            else:
                node1.left = node2.left
                
            if node1.right:
                stack.append((node1.right, node2.right))
            else:
                node1.right = node2.right
        
                
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # #add sum
        # t1.val += t2.val
        # t1.left = self.mergeTrees(t1.left, t2.left)
        # t1.right = self.mergeTrees(t1.right, t2.right)
        # return t1


