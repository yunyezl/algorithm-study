nk = input().split()
n = eval(nk[0])
k = eval(nk[1])
count = 0
while n != 1:
    if n >= k and n%k != 0:
        n = n-1
        count+=1
    elif n >= k and n % k == 0:
        n = n/k
        count+=1
print(count)
