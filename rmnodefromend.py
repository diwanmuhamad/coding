"""
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        start = ListNode()
        start.next = head
        fast = start
        slow = start

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next.next
        slow.next.next = None
        slow.next = temp

        return start.next  
