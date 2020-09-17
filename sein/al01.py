size, m ,k = map(int, input().split())

input_list = input().split()
input_list.sort()
list = []
for x in input_list :
    list.append(int(x))

sum, count = 0 , 0

for x in range(0,m) :
    for y in range(0,k) :
        if(count==m) : break
        count = count + 1
        sum = sum + list[-1]
    if(count==m) : break
    count = count + 1
    sum = sum + list[-2]

print(sum)

