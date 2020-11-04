n, m = map(int, input().split())
height_list = input().split()
height_list = [int (i) for i in height_list]
H = max(height_list)
s = 0

while s < m:
    sum = []
    s = 0
    for i in range(n):
        if height_list[i] - H >= 0:
            sum.append(height_list[i] - H)
    for j in range(len(sum)):
        s += sum[j]
    H -= 1
print(H + 1)