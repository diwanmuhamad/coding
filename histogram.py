input = [1,3,2,5,8,4,3]
maxx = input[0]

for i in range(len(input)):
    minn = input[i]
    count = 2
    maxx = max(maxx, minn)
    for j in range(i+1, len(input)):
        minn = min(minn, input[j])
        maxx = max(maxx, minn*count)

        count += 1

print(maxx)
    