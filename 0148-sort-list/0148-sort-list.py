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

        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        nums.sort()
        curr = head
        for i in nums:
            curr.val = i
            curr = curr.next
        return head