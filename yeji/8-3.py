n = int(input())
m = list(map(int, input().split()))

d = [0] * 101
d[0] = m[0]
d[1] = max(m[0], m[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + m[i])

print(d[n-1])
