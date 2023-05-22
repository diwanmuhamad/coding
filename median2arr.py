"""
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

"""

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    newArr = nums1 + nums2
    newArr.sort()

    if len(newArr) % 2 != 0:
        return newArr[(len(newArr) - 1) //2]
    
    median = (newArr[(len(newArr) - 1) //2] + newArr[(len(newArr) - 1) //2 + 1]) /2
    return median