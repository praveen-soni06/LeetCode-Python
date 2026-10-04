# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        nums.sort()
        dummy = ListNode()
        tail = dummy

        for i in nums:
            tail.next = ListNode(i)
            tail = tail.next
        return dummy.next