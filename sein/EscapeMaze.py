n, m = map(int, input().split())
gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input())))

visited = [[0 for i in range(m)] for j in range(n)]

# 상하좌우
lx = [-1, 1, 0, 0]
ly = [0, 0, -1, 1]

queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break

    for i in range(4):
        px = x + lx[i]
        py = y + ly[i]
        if px in range(0, n) and py in range(0, m) and visited[px][py] == 0 and gameMap[px][py] == 1:
            visited[px][py] = visited[x][y] + 1
            queue.append((px, py))