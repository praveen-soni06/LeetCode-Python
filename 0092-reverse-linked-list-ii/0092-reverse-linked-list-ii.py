# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head.next == None: return head
        # create a dummy node for balancing
        dummy = ListNode(0)
        dummy.next = head

        # point to the left 
        prevL = dummy
        for i in range(1,left):
            prevL = prevL.next

        start = prevL.next
        
        # reversing the range part
        prev = None
        curr = start
        for i in range(left , right+1):
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        # make the connection
        prevL.next = prev
        start.next = curr

        # return the head
        return dummy.next
                