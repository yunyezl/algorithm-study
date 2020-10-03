n, m = map(int, input().split())
ice_frame = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice_frame[x][y] == 0:
        ice_frame[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

icecream = 0

for x in range(n):
    for y in range(m):
        if ice_frame[x][y] == 0:
            if dfs(x, y) == True:
                icecream += 1

print(icecream)
