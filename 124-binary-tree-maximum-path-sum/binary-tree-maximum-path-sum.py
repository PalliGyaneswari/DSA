# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.r=float('-inf')
        def sumi(node):
            if node is None:
                return 0
            ls=max(0,sumi(node.left))
            rs=max(0,sumi(node.right))
            self.r=max(self.r,node.val+ls+rs)
            return node.val+max(ls,rs)
        sumi(root)
        return self.r
        