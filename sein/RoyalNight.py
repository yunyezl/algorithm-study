x , y = input()
x = ord(x) - ord('a')
y = int(y) - 1

count = 0
move = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1)]

for i in move:
    px = x + i[0]
    py = y + i[1]
    if px in range(0, 8) and py in range(0, 8):
        count = count + 1

print(count)
