"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

"""

class Solution:
    def countAndSay(self, n: int) -> str:

        def sayrec(n: int) -> str:
            if n == 1:
                return "1"
            
            nums = sayrec(n-1)
            fil = []
            newNums = ""
            i = 0
            while i < len(nums):
                count = 1
                k = i
                isTrue = True
                for j in range(i+1,len(nums)):
                    if nums[j] == nums[i]:
                        count += 1
                        if j == len(nums) - 1:
                            i = j+1
                    else:
                        i = j
                        isTrue = False
                        break
                newNums += str(count) + nums[k]
                if i == len(nums) - 1 and isTrue:
                    i += 1
            return newNums
        

        return sayrec(n)
            