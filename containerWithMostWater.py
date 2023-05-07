"""
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    leetcode problems
"""    

def maxArea(self, height: List[int]) -> int:
    i, j = 0, len(height) - 1

    area = min(height[i],height[j]) * (len(height) - 1)

    while i < j:
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
        
        newArea = min(height[i],height[j]) * (j-i)

        if newArea > area:
            area = newArea
    return area