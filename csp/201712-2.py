n, k = map(int, input().split())
q = []
for i in range(1, n+1):
    q.append(i)
t = 1
u = 1
while q:
    u=q.pop(0)
    if t%k==0 or t%10==k:
        pass
    else:
        q.append(u)
    t += 1
print(u)
