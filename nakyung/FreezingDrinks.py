nm = input().split()
n = int(nm[0])
m = int(nm[1])
grid = [list(map(int, input())) for _ in range(n)]

result = 0

def freesingdrink(x, y):
    grid[x][y] = 9
    a = [-1, 0, 1, 0]
    b = [0, 1, 0,-1]
    for i in range(4):
        if n-1 >= x+a[i] >= 0 and m-1 >= y+b[i] >= 0:
            if grid[x + a[i]][y + b[i]] == 0:
                freesingdrink(x + a[i], y + b[i])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            result += 1
            freesingdrink(i, j)

print(result)


