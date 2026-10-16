class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
            
        new_right = self.invertTree(root.left)
        new_left = self.invertTree(root.right)
        root.right = new_right
        root.left = new_left

        return root