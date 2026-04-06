# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currentOne = list1
        currentTwo = list2
        mergedList = ListNode("head")
        mergedCurrent = mergedList

        if list1 == None:
            return list2
        
        elif list2 == None:
            return list1


        while currentOne or currentTwo:
            if currentOne and not currentTwo:
                mergedCurrent.next = currentOne
                currentOne = currentOne.next
                mergedCurrent = mergedCurrent.next
            
            elif currentTwo and not currentOne:
                mergedCurrent.next = currentTwo
                currentTwo = currentTwo.next
                mergedCurrent = mergedCurrent.next

            elif currentOne.val <= currentTwo.val:
                mergedCurrent.next = currentOne
                currentOne = currentOne.next
                mergedCurrent = mergedCurrent.next
            else:
                mergedCurrent.next = currentTwo
                currentTwo = currentTwo.next
                mergedCurrent = mergedCurrent.next
        return mergedList.next


