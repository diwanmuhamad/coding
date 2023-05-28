"""
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    first = head

    temp = []

    while first:
        temp.append(first.val)
        first = first.next
    
    if len(temp) == 0:
        return None
        
    for i in range(0,len(temp),2):
        if i+1 <= len(temp) - 1:
            valTemp = temp[i]
            temp[i] = temp[i+1]
            temp[i+1] = valTemp
    
    second = ListNode()
    third = second

    for i in range(len(temp)):
        third.val = temp[i]
        if i < len(temp) - 1:
            third.next = ListNode()
            third = third.next
        else:
            third.next = None
    
    return second
            