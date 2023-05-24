"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tempArr = []

        for el in lists:
            while el:
                tempArr.append(el.val)
                el = el.next
        tempArr.sort()
        if len(tempArr) == 0:
            return None
        first = ListNode()
        second = first

        for j in range(len(tempArr)):
            first.val = tempArr[j]
            if j != len(tempArr) - 1:
                first.next = ListNode()
                first = first.next
            else:
                first.next = None
        
        return second