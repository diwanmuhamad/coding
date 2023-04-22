"""
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

def reverse(self, x: int) -> int:
        num = list(str(x))
        res = ""
        maxx = 2**31 - 1
        minn = -2**31
        if num[0] == "-":
            num = num[1:]
            num.reverse()
            res = "-" + "".join(num)
        else:
            num.reverse()
            res = "".join(num)
        if int(res) > maxx or  int(res) < minn:
            return 0
        return int(res)