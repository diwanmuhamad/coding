"""
    Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        cache = {x: nums.count(x) for x in nums}
        def backtrack():
            if len(nums) == len(perm):   
                res.append(perm.copy())
                return 
            
            for el in cache:
                if cache[el] > 0:
                    perm.append(el)
                    cache[el] -= 1
                    backtrack()
                    perm.pop()
                    cache[el] += 1
            
        
        backtrack()
        return res