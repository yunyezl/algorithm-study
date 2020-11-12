n = int(input())

array = [0] * 1001

d[1] = 1
d[2] = 2

for i in range(2, n+1):
    d[i] = (d[i-1] + 2 * d[i - 2]) % 796796

print(d[n])
