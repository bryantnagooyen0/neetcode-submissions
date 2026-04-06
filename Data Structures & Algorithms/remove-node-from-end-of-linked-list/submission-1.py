# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Reverse the linked list
            previous pointer
            current pointer
            next pointer
            save current.next under next
            current.next = prev
            move current and previous 1 step forward
        Starting from back move n nodes from back,
        remove nth node
        reverse list again
        return head
        """

        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        #prev is now head of list

        dummyNode = ListNode(0, prev)
        current = dummyNode

        for _ in range(n-1):
            current = current.next
        current.next = current.next.next

        prev = None
        current = dummyNode.next

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev






