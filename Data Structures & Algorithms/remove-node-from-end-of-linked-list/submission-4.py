# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        nFromBeg = length - n

        print("LENGTH ", length)
        print("FromBeg ", nFromBeg)

        if nFromBeg == 0:
            return head.next

        cur = head
        for i in range(length - 1):
            if (i + 1) == nFromBeg:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head


# 4, 6, 2, 1, 5 || n = 2 e= 1

#5 - 2 + 1 = 4