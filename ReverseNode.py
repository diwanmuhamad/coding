"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []

        first = head
        while first:
            temp.append(first.val)
            first = first.next
        if len(temp) == 0:
            return None

        i = 0
        while i + k <= len(temp):
            rev = temp[i:i+k]
            rev.reverse()
            temp = temp[0:i] + rev + temp[i+k:]
            i += k
        
        second = ListNode()
        third = second

        for j in range(len(temp)):
            third.val = temp[j]
            if j < len(temp) - 1:
                third.next = ListNode()
                third = third.next
            else:
                third.next = None
        
        return second