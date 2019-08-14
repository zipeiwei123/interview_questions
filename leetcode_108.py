"""Nums is already sorted, use iterative"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#         root = TreeNode(nums[len(nums)//2])
#         stack = [(root, nums)]
        
#         while stack:
#             cur, nums = stack.pop()
#             middle = len(nums)//2
    
#             left = nums[:middle]
#             if not left:
#                 cur.left = None
#             else:
#                 cur.left = TreeNode(left[len(left)//2])
#                 stack.append((cur.left, left))
            
#             right = nums[middle+1:]
#             if not right:
#                 cur.right = None
#             else:
#                 cur.right = TreeNode(right[len(right)//2])
#                 stack.append((cur.right, right))

#         return root
        #special case
        if not nums:
            return None
        root = TreeNode(nums[len(nums)//2])
        #push root on stack
        stack = [(root, nums)]
        #while the stack is append the current list, thus keep tracking the list until the list to None
        while stack:
            current_node, current_list = stack.pop()
            middle = len(current_list)//2
            
            left = current_list[:middle]
            #is left not exist in nums
            if not left:
                #if left not exist
                current_node.left = None
            else:
                #create new node
                current_node.left = TreeNode(left[len(left)//2])
                stack.append((current_node.left, left))
            
            right = current_list[middle+1:]
            if not right:
                current_node.right = None
            else:
                current_node.right = TreeNode(right[len(right)//2])
                stack.append((current_node.right, right))
        return root
        
        