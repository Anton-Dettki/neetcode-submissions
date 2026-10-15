# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        

        if not head:
            return None
        if not head.next:
            return head

        prev = head
        node = head.next
        nxt = node.next

        prev.next = None

        while node:
            node.next = prev
            prev = node
            node = nxt
            if node:
                nxt = node.next

        return prev

        #0 > 1 > 2 > 3
        #0(prev) > 1(node) > 2(nxt) > 3
        #None < 0(prev) > 1(node) > 2(nxt) > 3 line 14
        #None < 0(prev) < 1(node) 2(nxt) > 3 line 17
        #None < 0 < 1(prev) 2 (node) > 3 (nxt)

        #None < 0 < 1(prev) < 2 (node) 3 (nxt)
        


            



        #1(prev)  3(node) -> 4(nxt) -> 7

        # 1(prev) <- 3(node) 4(nxt) ->


