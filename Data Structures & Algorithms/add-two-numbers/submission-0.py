# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1str = ""
        while l1:
            l1str += str(l1.val)
            l1 = l1.next

        l2str = ""
        while l2:
            l2str += str(l2.val)
            l2 = l2.next
        summ = str(int(l1str[::-1]) + int(l2str[::-1]))

        newHead = dummy = ListNode()

        for i, c in enumerate(reversed(summ)):
            dummy.val = int(c)

            if i < len(summ) - 1:
                dummy.next = ListNode()
                dummy = dummy.next

        return newHead




