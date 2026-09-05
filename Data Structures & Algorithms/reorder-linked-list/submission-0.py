# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None

        prev = None
        curr = fast

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l1 = head
        l2 = prev

        while l1 and l2:
            temp = l1.next
            l1.next = l2

            temp2 = l2.next
            l2.next = temp

            l1 = temp;
            l2 = temp2;







