def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
store = list(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

store.sort()

for i in range(m):
    result = binary_search(store, order[i], 0, n - 1)
    if result == None:
        print("no", end=' ')
    else :
        print(result, end=' ')
