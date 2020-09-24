n, m = map(int, input().split()) # 게임맵의 크기 지정
visited = [[0] * m for _ in range(n)] # 방문한 적이 있는지 없는지를 카운트하기 위해 게임맵의 크기만큼 0으로 초기화
k, j, d = map(int, input().split()) # 캐릭터의 위치와 캐릭터가 바라보고 있는 방향
gameMap = [[int(n) for n in input().split()] for m in range(m)]
count = 1
turn_count = 0
visited[k][j] = 1 # 처음 캐릭터가 있는 곳 방문 체크

def left(d):
    d -= 1
    if d == -1:
        d = 3
    return d

#(-1,0) (0,1) (1,0) (0,-1) 캐릭터의 기본 위치에서 괄호안의 각 숫자를 더하면 순서대로 북/동/남/서 로 이동함 (왼쪽으로 이동)
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]

while True:
    d = left(d) # 무조건 한번 돌림
    px = k + x[d]
    py = j + y[d]
    if gameMap[px][py] == 0 and visited[px][py] == 0: # 돌린 방향으로 이동했을때 0이고, 한번도 방문한 적이 없다면
        visited[px][py] = 1 # 중복 카운트 방지
        k = px
        j = py # 실제로 이동시킴
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    if turn_count == 4: # 네 번 돌았는데 아무데도 가지 못함 (4면이 바다로 둘러쌓임)
        px = k - x[d]
        py = j - y[d] #후진
        if gameMap[px][py] == 0: #뒤로 갈 수 있다면(방문했어도 후진은 가능. 카운트 안하면 됨)
            k = px
            j = py
        else: #후진 불가
            break
        turn_count = 0 #뒤로 가기 성공한 경우 새로운 좌표의 turn_count

print(count)
