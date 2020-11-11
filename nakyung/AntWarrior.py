n = int(input())
k = list(map(int, input().split()))
food = [0] * 100

food[0] = k[0]
food[1] = max(k[0], k[1])
for i in range(2, n):
    food[i] = max(food[i-1], k[i] + food[i-2])

print(max(food))