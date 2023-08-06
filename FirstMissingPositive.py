"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        currNum = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            elif nums[i] == currNum:
                currNum += 1
                continue
            elif nums[i] != currNum:
                break
        return currNum