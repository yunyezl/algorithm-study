n = int(input())
list = [input() for _ in range(n)]

list.sort()
list.reverse()

for i in list:
    print(i, end=' ')