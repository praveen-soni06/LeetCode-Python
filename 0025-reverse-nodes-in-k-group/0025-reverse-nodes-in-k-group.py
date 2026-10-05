# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        def listLength(head):
            l = 0
            temp = head
            while temp:
                temp = temp.next
                l += 1
            return l

        def reverseKgroup(head, k, length):
            if length < k:
                return head

            count = 0
            prev, curr, nex = None, head, None
            while curr and count < k:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
                count += 1

            if nex:
                head.next = reverseKgroup(nex, k, length - k)

            return prev


        length = listLength(head)
        return reverseKgroup(head, k, length)