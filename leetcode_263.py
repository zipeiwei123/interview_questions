"""Changes from mini to max 
    Recusive/Iterative
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Wrong, no need"""        
        # if not root or not root.left or not root.right:
        #     return root
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
#         if not root:
#             return None
      
#         stack = []
#         stack.append(root)
      
#         while stack:
#             #pop the current node
#             node = stack.pop()
#             #swap the childern
#             temp = node.left
#             node.left = node.right
#             node.right = temp
            
#             if node.left:
                
#                 stack.append(node.left)
                
#             if node.right:
                
#                 stack.append(node.right)
#         return root
        
                