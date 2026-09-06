# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
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


        def findSame(t1):
            if t1 == None:
                return False

            if isSame(t1, subRoot):
                return True

            return findSame(t1.left) or findSame(t1.right)

            


        return findSame(root)