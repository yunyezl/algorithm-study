n = int(input())
dic = {}

for _ in range(n):
    name_score = input().split()
    dic[name_score[0]] = eval(name_score[1])

k = list(dic.keys())

for i in range(n-1):
    if dic[k[i]] > dic[k[i+1]]:
        k[i], k[i+1] = k[i+1], k[i]

for i in k:
    print(i, end=' ')