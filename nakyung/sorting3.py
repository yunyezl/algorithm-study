n, k = map(int, input().split())
a = input().split()
b = input().split()
sum = 0

a.sort()
b.sort()
b.reverse()

for i in range(k):
    a[i], b[i] = b[i], a[i]

for j in a:
    sum += int(j)

print(sum)
