n = int(input())
dic = {}

for x in range(n):
    name, score = input().split()
    dic[name] = int(score)

dic = sorted(dic.items(),reverse=True, key=lambda item: item[1])

for i in dic :
    print(i[0], end=' ')