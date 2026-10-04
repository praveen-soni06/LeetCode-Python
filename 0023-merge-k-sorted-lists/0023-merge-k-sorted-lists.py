import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        # solving via heap
        # heap = []

        # for i, node in enumerate(lists):
        #     if node:
        #         heapq.heappush(heap, (node.val, i, node))

        # dummy = ListNode()
        # curr = dummy

        # while heap:
        #     val, i, node = heapq.heappop(heap)

        #     curr.next = node
        #     curr = curr.next
        #     node = node.next

        #     if node:
        #         heapq.heappush(heap, (node.val, i, node))

        # return dummy.next


        # below is the easy way to do this without heap

        nums = []
        for i in lists:
            while i:
                nums.append(i.val)
                i = i.next

        nums.sort()
        result = ListNode()
        temp = result
        for i in nums:
            temp.next = ListNode(i)
            temp = temp.next

        return result.next