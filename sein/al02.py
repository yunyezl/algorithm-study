n ,m = map(int, input().split())

list = []
for x in range(0, n) :
    inputList = input().split()
    inputList.sort()
    list.append(inputList)

minList = []
for x in list :
    minList.append(x[0])
print(max(minList))
