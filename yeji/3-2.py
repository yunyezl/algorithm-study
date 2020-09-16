# 큰 수의 법칙
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K(배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과할 수 없음)

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
array.reverse()

max = array[0]
max2 = array[1]
sum = 0
count = 0

while True:
    for i in range(k): 
        if count == m: break
        sum += max
        count = count + 1
    if count == m: break    
    sum += max2
    count = count + 1

print(sum)