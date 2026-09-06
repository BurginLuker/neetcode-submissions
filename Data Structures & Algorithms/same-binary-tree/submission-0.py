# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(t1, t2):
            if t1 == None and t2 == None:
                return True

            if t1 and t2 == None:
                return False
            if t2 and t1 == None:
                return False

            left = isSame(t1.left, t2.left)
            right = isSame(t1.right, t2.right)

            return t1.val == t2.val and left and right
            

        return isSame(p, q)