# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]

        out = []
        while len(queue) > 0:
            temp = []
            nextQ = []
            for node in queue:
                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
                temp.append(node.val)
                
            out.append(temp)
            queue = nextQ

        return out
