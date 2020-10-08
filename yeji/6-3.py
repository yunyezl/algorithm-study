n = int(input())
dic = { }

for i in range(n):
    name, score = input().split()
    dic[name] = int(score)

sortdict= sorted(dic.items(), key=lambda x: x[1]) #튜플로 값 반환

for i in sortdict:
    print(i[0][0], end=' ')
    

# 계수 정렬
n = int(input())
dic = { }
array = []

for i in range(n):
    name, score = input().split()
    dic[name] = int(score)
    array.append(int(score))

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

