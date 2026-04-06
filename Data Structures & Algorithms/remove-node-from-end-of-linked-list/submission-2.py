# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Traverse the list once to compute total nodes N.
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        #Compute removeIndex = N - n.
        removeIndex = N - n

        #If removeIndex == 0, delete the head → return head.next.
        if removeIndex == 0:
            head = head.next
            return head
        #Traverse again until reaching the node before removeIndex.
        pointer = head
        index = 1
        while index < removeIndex:
            pointer = pointer.next
            index += 1
        
        pointer.next = pointer.next.next

        return head


        #Update its next pointer to skip the unwanted node.
        #Return the modified head.
        