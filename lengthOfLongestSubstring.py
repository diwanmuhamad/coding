"""
    lengthOfLongestSubstring
    Problems:
    Given a string s, find the length of the longest 
    substring
    without repeating characters.

    source from Leetcode

"""

s = input()

el_set = set()
maxx, start = 0, 0

for i, el in enumerate(s):
    while el in el_set:
        el_set.remove(s[start])
        start += 1
    el_set.add(el)
    maxx = max(maxx, i - start + 1)
print(maxx)