# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            sum = d1 + d2 + carry
            carry = sum // 10 
            ank = sum % 10 

            tail.next = ListNode(ank)

            tail = tail.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
            
        tail.next = ListNode(carry) if carry>0 else None
        return dummy.next