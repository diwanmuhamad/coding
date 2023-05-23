"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(right, left, n, s):
            if len(s) == n*2:
                res.append(s)
                return
            
            if left < n:
                dfs(right, left+1, n, s + "(")
            
            if right < left:
                dfs(right+1, left, n, s+")")

            return
        
        dfs(0,0,n, '')

        return res