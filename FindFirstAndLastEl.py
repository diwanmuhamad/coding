"""
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

"""


def searchRange(self, nums: List[int], target: int) -> List[int]:
    res = [-1, -1]

    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first = True

            if nums[right] == target:
                res[1] = right
            for i in range(left, right+1):
                if first and nums[i] == target:
                    res[0] = i
                    first = False
                elif not first and nums[i] != target:
                    res[1] = i - 1
                    break
            break

            
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == right and nums[left] == target:
        return [left, right]
    return res