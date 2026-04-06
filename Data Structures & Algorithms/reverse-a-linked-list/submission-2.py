# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        array = []
        pointer = head
        
        while pointer != None:
            array.append(pointer.val)
            pointer = pointer.next
        
        new_head = ListNode(array[len(array) - 1])
        new_pointer = new_head
        for i in range(len(array) - 2, -1, -1):
            new_pointer.next = ListNode(array[i])
            new_pointer = new_pointer.next
        
        return new_head
            
        