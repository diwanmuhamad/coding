"""
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.
"""

nums = [1,1,1,0]
target = -100
nums.sort()

summ = nums[0] + nums[1] + nums[len(nums)-1]
for i in range(len(nums) - 2):
    first = nums[i]
    start = i+1
    last = len(nums)-1
    while start < last:
        tempSum = first + nums[start] + nums[last]
        if tempSum == target:
            print(tempSum, "tp2")
        if abs(tempSum - target) < abs(summ - target):
            summ = tempSum

        if tempSum < target:
            start += 1
        elif tempSum > target:
            last -= 1

print(summ)