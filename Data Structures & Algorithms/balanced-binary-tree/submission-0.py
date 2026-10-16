# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(curr):
            if not curr:
                return 0

            leftTree = dfs(curr.left)
            rightTree = dfs(curr.right)

            diff = abs(leftTree - rightTree)

            if diff > 1:
                self.isBalanced = False

            return 1 + max(leftTree, rightTree)
        
        dfs(root)
        return self.isBalanced