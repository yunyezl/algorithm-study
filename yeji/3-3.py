# N X M 형태로 놓여있는 카드
# 각 행에서 숫자가 가장 낮은 카드를 뽑음
# N개의 카드 중 가장 큰 수를 구함

n, m = map(int, input().split())
array = [[int(x) for x in input().split()] for y in range(n)] # 이차원 배열 입력받는 식
array2 = []
min = array[0][0]

for i in range(n):
    for j in range(m):
        if array[i][j] < min:
            min = array[i][j]
    array2.append(min)
    min = array[i][j]        

print(max(array2))
