#수평으로 두 칸 이동 후 수직으로 한 칸
#수직으로 두 칸 이동 후 수평으로 한 칸
n = input()
count = 0

x, y = 1, 1
move = [[1,2],[2,1],[-1,-2],[-2,-1],[1,-2],[-1,2],[2,-1],[-2,1]]
for i,j in move :
    nx = ord(n[0]) - 96
    ny = int(n[1])
    nx = nx + i
    ny = ny + j
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8 :
        count+=1

print(count)