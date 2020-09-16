# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

n, k = map(int, input().split())

count = 0

while n != 1:
    if n % k == 0:
        n = n / k
        count += 1
    else:
        n -= 1
        count += 1

print(count)
