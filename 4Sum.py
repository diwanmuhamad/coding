"""
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
"""

nums= [0,0,0,0]
target = 0

if len(nums) < 4:
    print([])
res = set()
nums.sort()
for i in range(len(nums)-3):
    print(i)
    for j in range(i+1,len(nums)-2):
        start = j+1
        end = len(nums)-1
        while start < end:
            tempSum = nums[i] + nums[j] + nums[start] + nums[end]
            print(tempSum)
            if tempSum == target:
                res.add((nums[i], nums[j], nums[start], nums[end]))
                end -= 1
            elif tempSum < target:
                start += 1
            else:
                end -= 1
print(res)