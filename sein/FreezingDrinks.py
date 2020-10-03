n, m = map(int, input().split())
freezimgMap = []
visited = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    freezimgMap.append(list(map(int, input())))
visited[0][0] = 1

# 상하좌우
lx = [-1, 1, 0, 0]
ly = [0, 0, -1, 1]

def dfs(x, y):
    if x not in range(0, n) or y not in range(0, m):
        return False

    if freezimgMap[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(4):
            px = x + lx[i]
            py = y + ly[i]
            dfs(px, py)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)