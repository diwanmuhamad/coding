#find the numbers of unique string from removing 2 consecutive letters from the string


testCase = int(input())

for i in range(testCase):
    length = int(input())
    s = input()
    countRepeat = 0
    for j in range(2, length):
        if s[j] == s[j-2]:
            countRepeat += 1
    print(length - 1 - countRepeat)

