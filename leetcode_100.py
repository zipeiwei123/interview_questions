# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Iterative"""
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            #check current node if the condition met
            if not self.check_two_nodes(p, q):
                return False
            if p:
                #check for the child node
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        return True
        
        # #if two node are both none
        # if not p and not q:
        #     return True
        # #if p node or the q node has value
        # if not p or not q:
        #     return False
        # #check if two nodes are equal
        # if p.val != q.val:
        #     return False
        # #check their children
        # return self.isSameTree(p.right, q.right) and \
        #        self.isSameTree(p.left, q.left)
    
    def check_two_nodes(self, p, q):
        if not p and not q:
            return True
        #if p node or the q node has value
        if not p or not q:
            return False
        #check if two nodes are equal
        if p.val != q.val:
            return False
        #return true is all the condition met
        return True