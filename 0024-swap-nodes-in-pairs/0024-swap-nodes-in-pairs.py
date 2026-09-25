# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs 
            nextPair = curr.next.next
            new = curr.next

            # reverse 
            new.next = curr
            curr.next = nextPair
            prev.next = new

            # update ptr
            prev = curr
            curr = nextPair

        return dummy.next