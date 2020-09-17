nmk = input().split()

if eval(nmk[0]) >= 2 and eval(nmk[0]) <= 1000 :
    n = eval(nmk[0])
if eval(nmk[1]) >= 1 and eval(nmk[1]) <= 10000 :
    m = eval(nmk[1])
if eval(nmk[2]) >= 1 and eval(nmk[2]) <= 10000 and eval(nmk[2]) <= m :
    k = eval(nmk[2])

i = 0
num = input().split()
num = num[:n]

num.sort()

sum = eval(num[n-1])*k*int(m/k) + eval(num[n-2])*int(m%k)

print(sum)