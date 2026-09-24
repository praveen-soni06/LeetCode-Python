# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        prev = None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp 
            temp = front

        head = prev

        dummy = ListNode(0)
        dummy.next = head

        ptr = dummy
        for i in range(1, n):
            ptr = ptr.next

        ptr.next = ptr.next.next
        
        prev = None
        temp = dummy.next
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp 
            temp = front

        head = prev

        return head
