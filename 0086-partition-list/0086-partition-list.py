# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        t2 = dummy

        dummy2 = ListNode(0)
        tail = dummy2

        while t2 and t2.next:
            if t2.next.val < x:
                tail.next = ListNode(t2.next.val)
                t2.next = t2.next.next
                tail = tail.next
            else: 
                t2 = t2.next
        t1 = dummy.next
        while t1:
            tail.next = ListNode(t1.val)
            t1 = t1.next
            tail = tail.next

        return dummy2.next
        

