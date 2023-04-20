"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

problem from leetcode

"""
def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        count = 1
        sign = "+"

        cache = {j: [] for j in range(1, numRows + 1)}

        for char in s:
            if count == 1:
                sign = "+"
            if count == numRows:
                sign = "-"

            cache[count].append(char)

            if sign == "+":
                count += 1
            elif sign == "-":
                count -= 1
        
        res = ""
        for el in cache:
            res += "".join(cache[el])
        return res
