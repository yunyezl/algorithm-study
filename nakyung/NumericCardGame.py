nm = input().split()
n = eval(nm[0])
m = eval(nm[1])

i = 0
small = 0
while i < n:
    numN = input().split()
    numN = numN[:m]
    numN.sort()
    while eval(numN[0]) > small:
        small = eval(numN[0])
    i += 1

print(small)


