"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for x in nums]

        def backtrack(res, nums, perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return res
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                    backtrack(res, nums, perm, used)
                    used[i] = False
                    perm.pop()
        
        backtrack(res, nums, [], used)
        return res