"""
    Hard leetcode problems
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).
""" 

def isMatch(self, s: str, p: str) -> bool:
        i, j = 0,0
        cache = {}

        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False

            match = (i < len(s) and (s[i] == p[j] or p[j] == "."))

            if (j+1 < len(p) and p[j+1] == "*"):
                cache[(i,j)] = (dfs(i, j+2)
                                or (match and dfs(i+1, j)))
                return cache[(i,j)]

            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]

            cache[(i,j)] = False
            return False  
        return dfs(0,0)