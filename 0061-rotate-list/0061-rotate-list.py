# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        temp = head
        n = 1
        while temp.next:
            temp = temp.next
            n += 1
        temp.next = head   # make circular linkedlist

        # handel k
        k = k % n

        # find new tail (n-k-1)
        steps = n-k-1

        new_temp = head
        for _ in range(steps):
            new_temp = new_temp.next
        
        new_head = new_temp.next
        new_temp.next = None  # cut list

        return new_head

        