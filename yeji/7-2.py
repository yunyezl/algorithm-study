global h
h = 0

def search(array, m, start, end): 
    global h
    slideDduckList = []

    for i in range(end+1):
        if (array[i] - h > 0):
            slideDduck = array[i] - h
        else:
            slideDduck = 0
        slideDduckList.append(slideDduck)

    if sum(slideDduckList) == target :
        print(h)
        return -1
    else:
        h = h + 1
        search(array, target, start, end) 

n, m = map(int, input().split())
dduck = list(map(int, input().split()))

dduck.sort()
search(dduck, m, 0, n - 1)
