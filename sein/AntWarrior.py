n = int(input())
k = list(map(int, input().split()))

dy = [0] * 100

dy[0] = k[0]
dy[1] = max(k[0], k[1])

for i in range(2,n) :
    if dy[i - 1] > dy[i - 2] + k[i] :
        dy[i] = dy[i - 1]
    else:
        dy[i] = dy[i - 2] + k[i]

print(dy[n - 1])