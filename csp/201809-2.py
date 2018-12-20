# [1, 5, 9, 14]
# [3, 6, 13, 15]
# [2, 5, 10, 13]
# [4, 7, 11, 14]

n = int(input())
m = 2*n
start = []
stop = []
for i in range(m):
    a,b = list(map(int, input().split()))
    start.append(a)
    stop.append(b)
H_start = start[0:n]
H_stop = stop[0:n]
W_start = start[n:m]
W_stop = stop[n:m]
time = 0
for i in range(n):
    for j in range(n):
        if W_stop[j] <= H_start[i]:
            continue
        elif W_start[j] <= H_start[i] and W_stop[j] <= H_stop[i]:
            time += W_stop[j] - H_start[i]
            continue
        elif W_start[j] <= H_start[i] and W_stop[j] >= H_stop[i]:
            time += H_stop[i] - H_start[i]
            break
        elif W_start[j] >= H_stop[i]:
            break
        elif W_start[j] >= H_start[i] and W_stop[j] <= H_stop[i]:
            time += W_stop[j] - W_start[j]
            continue
        elif W_start[j] >= H_start[i] and W_stop[j] >= H_stop[i]:
            time += H_stop[i] - W_start[j]
            break

print(time)