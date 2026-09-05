# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head
        while curr:
            i += 1
            curr = curr.next

        curr = head
        prev = None
        dummy = ListNode(None, head)
        
        for x in range(i - n + 1):
            if x == i - n:
                temp = curr.next
                curr.next = None
                if prev:
                    prev.next = temp
                else:
                    dummy.next = temp
            else:
                prev = curr
                curr = curr.next

        return dummy.next






