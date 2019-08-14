# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self.generate_tree(1, n)
    
    #a dp way to create tree
    def generate_tree(self, start, end):
        #base condition
        if start > end:
            return [None,]
        trees = []
        #pick up a root, cartesian generate left and right
        for i in range(start , end+1):
            left_tree = self.generate_tree(start, i-1)
            right_tree = self.generate_tree(i+1, end)
            #connect left and right
            for l in left_tree:
                for r in right_tree:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    trees.append(node)
        return trees
        