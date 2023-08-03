"""
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        newNums = nums[:]
        newNums = sorted(newNums, reverse=True)
        if str(newNums) == str(nums):
            nums.sort()
            return

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                count = 0
                temps = nums[i-1]
                for j in range(i+1, len(nums)):
                    if nums[j] < nums[i] and nums[j] > temps:
                        if count == 0:
                            temp = nums[j]
                            nums[j] = nums[i-1]
                            nums[i-1] = temp
                            count += 1
                        elif nums[j] - temps < nums[i-1] - temps and count > 0:
                            temp = nums[j]
                            nums[j] = nums[i-1]
                            nums[i-1] = temp
                            count += 1

                if count == 0:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = temp
                
                countGreater = 1
                while countGreater != 0:
                    countGreater = 0
                    for k in range(i, len(nums)-1):
                        if nums[k] > nums[k+1]:
                            temp = nums[k]
                            nums[k] = nums[k+1]
                            nums[k+1] = temp
                            countGreater += 1
                break