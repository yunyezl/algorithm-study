n = int(input())
list = []

for _ in range(n):
    list.append(int(input()))

list.sort()
list.reverse()

for i in list:
    print(i, end=' ')