n, L, t = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [1 for i in a]
for i in range(t):
    for j in range(n):
        #如果小球到了起点或者终点，改变方向
        if (a[j]==0 and b[j]==-1) or (a[j]==L and b[j]==1):
            b[j]*=-1
        else:
            #当小球相撞时，两个小球的方向都改变一次
            for k in range(n):
                if a[k]==a[j] and k != j:
                    b[k]*=-1
                    b[j]*=-1
        #更新小球位置
        a[j]+=b[j]
for i in a:
    print(i, end=' ')
