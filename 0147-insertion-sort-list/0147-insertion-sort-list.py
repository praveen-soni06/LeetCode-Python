# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        arr =[]
        while head:
            arr.append(head.val)
            head = head.next
        dummy= ListNode(0)
        curr = dummy
        arr.sort()
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next