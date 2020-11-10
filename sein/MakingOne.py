x = int(input())

dy = [0] * 300000

for i in range(2, x + 1):

    dy[i] = dy[i - 1] + 1

    if i % 2 == 0:
        if dy[i] > dy[i // 2] + 1:
            dy[i] = dy[i // 2] + 1

    if i % 3 == 0:
        if dy[i] > dy[i // 3] + 1:
            dy[i] = dy[i // 3] + 1

    if i % 5 == 0:
        if dy[i] > dy[i // 5] + 1:
            dy[i] = dy[i // 5] + 1

print(dy[x])