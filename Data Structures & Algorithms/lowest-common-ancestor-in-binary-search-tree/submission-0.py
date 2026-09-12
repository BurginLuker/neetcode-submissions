# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(node):
            if not node or not p or not q:
                return None
            if max(p.val, q.val) < node.val:
                return search(node.left)
            elif min(p.val, q.val) > node.val:
                return search(node.right)
            else:
                return node

        
        return search(root)