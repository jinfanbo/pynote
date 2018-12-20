score = list(map(int, input().split()))
sum = 0
temp = 0
for i in score:
    if i == 1:
        temp = 0
        sum += 1
    elif i == 2:
        temp += 2
        sum += temp
    elif i == 0:
        break
print(sum)
