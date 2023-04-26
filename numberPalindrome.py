def isPalindrome(self, x: int) -> bool:
        string = str(x)
        string2 = list(string)
        string2.reverse()

        string2 = "".join(string2)
        if string == string2:
            return True
        return False