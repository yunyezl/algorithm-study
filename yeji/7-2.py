# global h
# h = 0

# def search(array, target, start, end): 
#     global h
#     slideDduckList = []

#     for i in range(end+1):
#         if (array[i] - h > 0):
#             slideDduck = array[i] - h
#         else:
#             slideDduck = 0
#         slideDduckList.append(slideDduck)

#     if sum(slideDduckList) == target :
#         print(h)
#         return -1
#     else:
#         h = h + 1
#         search(array, target, start, end) 

# n, m = map(int, input().split())
# dduck = list(map(int, input().split()))

# dduck.sort()
# search(dduck, m, 0, n - 1)

n, m = map(int, input().split())
dduck = list(map(int, input().split()))

start = 0
end = dduck[n-1]

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in dduck:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
