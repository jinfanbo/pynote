n = int(input())
num = list(map(int, input().split()))
num.sort()
min = abs(num[0] - num[1])
for i in range(1, len(num)-1):
    if abs(num[i] - num[i+1]) < min:
        min = abs(num[i] - num[i+1])
print(min)
