"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        q = []

        for el in s:
            if el in data:
                if len(q) == 0 or q[len(q)-1] != data[el]:
                    return False
                q.pop()
            else:
                q.append(el)
        
        if len(q) == 0:
            return True
        return False