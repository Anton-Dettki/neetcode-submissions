class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
            
        newRight = self.invertTree(root.left)
        newLeft = self.invertTree(root.right)

        root.left = newLeft
        root.right = newRight
        
        return root