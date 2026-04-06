# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Initialize dummy node
        have left pointer at dummy node
        loop right pointer to be n steps ahead of l pointer
        loop till right is at the end of list
        l.next = l.next.next
        return dummy.next
        """

        dummyNode = ListNode(0, head)
        l = dummyNode
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummyNode.next
