from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]

def search(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            px = x + mx[i]
            py = y + my[i]
            if px < 0 or px >= n or py < 0 or py >= m:
                continue
            if maze[px][py] == 1:
                maze[px][py] = maze[x][y] + 1
                queue.append((px, py))
    return maze[n - 1][m - 1]

print(search(0,0))
