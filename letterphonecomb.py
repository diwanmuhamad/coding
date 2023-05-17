"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

def letterCombinations(self, digits: str) -> List[str]:
    mapNumLetter = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    res = []

    if len(digits) == 1:
        letter = mapNumLetter[int(digits[0])]
        for el in letter:
            res.append(el)
    elif len(digits) == 2:
        letter1 = mapNumLetter[int(digits[0])]
        letter2 = mapNumLetter[int(digits[1])]
        for el in letter1:
            let = ""
            let += el
            for el2 in letter2:
                temp = let
                temp += el2
                res.append(temp)
    elif len(digits) == 3:
        letter1 = mapNumLetter[int(digits[0])]
        letter2 = mapNumLetter[int(digits[1])]
        letter3 = mapNumLetter[int(digits[2])]
        for el in letter1:
            let = ""
            let += el
            for el2 in letter2:
                temp = let
                temp += el2
                for el3 in letter3:
                    temp2 = temp
                    temp2 += el3
                    res.append(temp2)
    elif len(digits) == 4:
        letter1 = mapNumLetter[int(digits[0])]
        letter2 = mapNumLetter[int(digits[1])]
        letter3 = mapNumLetter[int(digits[2])]
        letter4 = mapNumLetter[int(digits[3])]
        for el in letter1:
            let = ""
            let += el
            for el2 in letter2:
                temp = let
                temp += el2
                for el3 in letter3:
                    temp2 = temp
                    temp2 += el3
                    for el4 in letter4:
                        temp3 = temp2
                        temp3 += el4
                        res.append(temp3)
    return res
