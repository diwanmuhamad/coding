"""
    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.

"""

def intToRoman(self, num: int) -> str:
        strNum = str(num)
        res = ""
        if len(strNum) == 4:
            for i in range(len(strNum)):
                if i == 0:
                    for j in range(int(strNum[i])):
                        res += "M"
                elif i == 1:
                    if strNum[i] == "9":
                        res += "CM"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "D"
                        for j in range(int(strNum[i]) - 5):
                            res += "C"
                    elif int(strNum[i]) == 4:
                        res += "CD"
                    else:
                        for j in range(int(strNum[i])):
                            res += "C"
                elif i == 2:
                    if strNum[i] == "9":
                        res += "XC"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "L"
                        for j in range(int(strNum[i]) - 5):
                            res += "X"
                    elif int(strNum[i]) == 4:
                        res += "XL"
                    else:
                        for j in range(int(strNum[i])):
                            res += "X"
                else:
                    if strNum[i] == "9":
                        res += "IX"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "V"
                        for j in range(int(strNum[i]) - 5):
                            res += "I"
                    elif int(strNum[i]) == 4:
                        res += "IV"
                    else:
                        for j in range(int(strNum[i])):
                            res += "I"
        elif len(strNum) == 3:
            for i in range(len(strNum)):
                if i == 0:
                    if strNum[i] == "9":
                        res += "CM"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "D"
                        for j in range(int(strNum[i]) - 5):
                            res += "C"
                    elif int(strNum[i]) == 4:
                        res += "CD"
                    else:
                        for j in range(int(strNum[i])):
                            res += "C"
                elif i == 1:
                    if strNum[i] == "9":
                        res += "XC"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "L"
                        for j in range(int(strNum[i]) - 5):
                            res += "X"
                    elif int(strNum[i]) == 4:
                        res += "XL"
                    else:
                        for j in range(int(strNum[i])):
                            res += "X"
                else:
                    if strNum[i] == "9":
                        res += "IX"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "V"
                        for j in range(int(strNum[i]) - 5):
                            res += "I"
                    elif int(strNum[i]) == 4:
                        res += "IV"
                    else:
                        for j in range(int(strNum[i])):
                            res += "I"
        elif len(strNum) == 2:
             for i in range(len(strNum)):
                if i == 0:
                    if strNum[i] == "9":
                        res += "XC"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "L"
                        for j in range(int(strNum[i]) - 5):
                            res += "X"
                    elif int(strNum[i]) == 4:
                        res += "XL"
                    else:
                        for j in range(int(strNum[i])):
                            res += "X"
                else:
                    if strNum[i] == "9":
                        res += "IX"
                    elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                        res += "V"
                        for j in range(int(strNum[i]) - 5):
                            res += "I"
                    elif int(strNum[i]) == 4:
                        res += "IV"
                    else:
                        for j in range(int(strNum[i])):
                            res += "I"
        else:
            i = 0
            if strNum[i] == "9":
                res += "IX"
            elif int(strNum[i]) < 9 and int(strNum[i]) >= 5:
                res += "V"
                for j in range(int(strNum[i]) - 5):
                    res += "I"
            elif int(strNum[i]) == 4:
                res += "IV"
            else:
                for j in range(int(strNum[i])):
                    res += "I"
        return res