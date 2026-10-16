# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        qList = []
        pList = []

        def preOrder(curr, xList):
            if not curr:
                xList.append("x")
                return 
                print(xList)
            xList.append(curr.val)
            
            preOrder(curr.left, xList)
            preOrder(curr.right, xList)    

        preOrder(p, pList)
        preOrder(q, qList)

        print(pList)
        print(qList)
        return pList == qList


            
            
            
        