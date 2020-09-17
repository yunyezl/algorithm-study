n ,k = map(int, input().split())

count = n % k
n = n - count
while n != 1 :
    n = n / k
    count = count +1

print(count)