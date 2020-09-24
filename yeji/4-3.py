n = input()
m = int(ord(n[0]))-int(ord('a'))

move = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1)]
count = 0

x = int(n[1])

for i in move:
    nx = x + i[0]
    ny = m + i[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and nx <= 8:
        count += 1

print(count)
