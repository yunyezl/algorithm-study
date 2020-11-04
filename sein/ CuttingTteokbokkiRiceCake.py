n, m = map(int, input().split())

input_N_list = list(map(int, input().split()))

mid = max(input_N_list)
min = 1

while ( True ) :
    sum = 0
    for x in input_N_list:
        y = x - mid
        if y < 0: y = 0
        sum = sum + y

    if sum == m:
        print(mid)
        break

    elif sum < m:
        max = mid
        mid = (mid + min) // 2

    elif sum > m:
        if sum in range(m, m + n-1):
            print(mid)
            break
        else:
            min = mid
            mid = (mid + max) // 2
