# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node,level,res):
            if node is None:
                return 0
            if len(res)<=level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left,level+1,res)
            dfs(node.right,level+1,res)
        r=[]
        dfs(root,0,r)
        return r
        