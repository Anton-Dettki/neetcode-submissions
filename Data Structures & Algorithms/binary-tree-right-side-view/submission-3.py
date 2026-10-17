# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        queue = deque([root])

        while queue:
            x = []
            for i in range(len(queue)):
                temp = queue.popleft()
                x.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            last = len(x) - 1
            lastElement = x[last]

            res.append(x[-1])

        return res
