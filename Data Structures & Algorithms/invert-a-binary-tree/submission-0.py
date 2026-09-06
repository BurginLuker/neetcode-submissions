# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            if node == None:
                return
            
            left = swap(node.left)
            right = swap(node.right)

            temp = node.left
            node.left = right
            node.right = temp

            return node

        
        swap(root)
        return root