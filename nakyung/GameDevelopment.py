nm = input().split()
n, m = eval(nm[0]), eval(nm[1])
abd = input().split()
b, a, d = eval(abd[0]), eval(abd[1]), eval(abd[2])
count = 1
board = [[int(x) for x in input().split()] for y in range(m)]

for i in board:
    for j in i:
        if board[a-1][b] == 1 and board[a][b-1] == 1 and board[a+1][b] == 1 and board[a][b+1] == 1:
            break
        if j == board[a][b]:
            if d == 0:
                if board[a-1][b] == 0:
                    count += 1
                a = a-1
                d = 3
            if d == 1 and board[a][b-1] == 0:
                if board[a][b-1] == 0:
                    count += 1
                b = b-1
                d = 0
            if d == 2:
                if board[a+1][b] == 0:
                    count += 1
                a = a+1
                d = 1
            if d == 3:
                if board[a][b+1] == 0:
                    count += 1
                b = b+1
                d = 2
print(count)

