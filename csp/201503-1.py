n, m = map(int, input().split())
grid = [[] for i in range(n)]
new_grid = [[] for i in range(m)]
for i in range(n):
    line = list(map(int, input().split()))
    grid[i].extend(line)
for i in grid:
        for j in range(m):
            new_grid[m-1-j].append(i[j])
for i in new_grid:
    for j in i:
        print(j, end=' ')
    print()
