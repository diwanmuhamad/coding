"""
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

"""

def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 or (len(s) == 1 and (s[0] == "+" or s[0] == "-")):
            return 0
        res = 0
        numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if ((s[0] == "-" or s[0] == "+") and s[1] not in numbers) or (s[0] not in numbers and (s[0] != "-" and s[0] != "+")):
            return res
        if s[0] == "-":
            res = "-"
            for i in range(1, len(s)):
                    if s[i] in numbers:
                        res += s[i]
                    else:
                        break
            res = int(res)
        else:
            res = ""
            if s[0] == "+":
                for i in range(1, len(s)):
                    if s[i] in numbers:
                        res += s[i]
                    else:
                        break
            else:
                for el in s:
                    if el in numbers:
                        res += el
                    else:
                        break
            
            res = int(res)
        
        maxx = 2**31 - 1
        minn = -2**31
        if res > maxx:
            return maxx
        if res < minn:
            return minn

        return res