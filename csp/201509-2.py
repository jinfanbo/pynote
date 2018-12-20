y = int(input())
d = int(input())
a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y%400==0 or (y%4==0 and y%100!=0):
    a[2] = 29
sum = 0
yue = 0
ri = 0
for i in range(1, 13):
    sum = sum + a[i]
    if d <= sum:
        yue = i
        ri = d-sum+a[i]
        break
print(yue)
print(ri)
