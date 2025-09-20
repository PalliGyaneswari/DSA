# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            lt=height(root.left)
            rt=height(root.right)
            return max(lt,rt)+1
        return height(root)
        